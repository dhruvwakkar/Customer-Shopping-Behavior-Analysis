import pandas as pd
import openpyxl
from sqlalchemy import create_engine

# ==========================================
# 1. READ EXCEL FILE
# ==========================================

df = pd.read_excel("customer_shopping_behavior_dataset.xlsx")


# ==========================================
# 2. FILLING MISSING VALUES
# ==========================================

df['Review Rating'] = (
    df.groupby('Category')['Review Rating']
      .transform(lambda x: x.fillna(x.median()))
)


# ==========================================
# 3. MODIFY HEADER (SNAKE CASE)
# ==========================================

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

df = df.rename(columns={
    'purchase_amount_(inr)': 'purchase_amount'
})


# ==========================================
# 4. CREATE COLUMN: age_group
# ==========================================

labels = ["young-adult", "adult", "middle-aged", "senior"]

df['age_group'] = pd.qcut(
    df['age'],
    q=4,
    labels=labels
)


# ==========================================
# 5. CREATE COLUMN: purchase_frequency_days
# ==========================================

frequency_days = {
    'Weekly': 7,
    'Fortnightly': 14,
    'Monthly': 30,
    'Quarterly': 90,
    'Every 3 Months': 90,
    'Bi-Weekly': 14,
    'Annually': 365
}

df["purchase_frequency_days"] = (
    df["frequency_of_purchases"].map(frequency_days)
)


# ==========================================
# 6. DROP UNWANTED COLUMN
# ==========================================

df = df.drop("promo_code_used", axis=1)


# ==========================================
# 7. SAVE CLEANED DATA TO EXCEL
# ==========================================

df.to_excel(
    "customer_shopping_behavior_cleaned.xlsx",
    index=False
)


# ==========================================
# 8. CONNECT TO MYSQL
# ==========================================

engine = create_engine(
    "mysql+pymysql://root:Dhruvwakkar16@localhost:3306/customer_shopping"
)


# ==========================================
# 9. SEND DATA TO MYSQL
# ==========================================

df.to_sql(
    "customer_shopping",
    con=engine,
    if_exists="replace",
    index=False
)


print("===================================")
print("Data cleaning completed!")
print("Cleaned Excel file saved!")
print("Data successfully imported into MySQL!")
print("===================================")