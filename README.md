# Customer Shopping Behavior Analysis | Python, MySQL & Power BI

## 📊 Project Overview

This project analyzes customer shopping behavior to identify purchasing patterns, customer segments, product performance, discount usage, subscription behavior, and revenue trends.

The project follows an end-to-end data analytics workflow:

**Raw Dataset → Python Data Cleaning → Excel → MySQL → SQL Analysis → Power BI Dashboard**

The goal is to transform raw customer shopping data into meaningful business insights using commonly used data analytics tools.

---

## 🎯 Business Objectives

The analysis focuses on answering key business questions such as:

- How does revenue differ between male and female customers?
- Which customers used discounts but still spent more than the average purchase amount?
- Which products have the highest average review ratings?
- How does average spending differ between Standard and Express shipping?
- Do subscribed customers spend more than non-subscribers?
- Which products rely most heavily on discounts?
- How can customers be segmented into New, Returning, and Loyal customers?
- What are the top 3 products within each category?
- Are repeat buyers more likely to subscribe?
- Which age groups contribute the most revenue?

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data cleaning and transformation |
| Pandas | Data manipulation and analysis |
| Excel | Cleaned dataset storage |
| MySQL | Database storage |
| SQL | Business analysis and querying |
| Power BI | Data visualization and dashboard creation |

---

## 🔄 Project Workflow

### 1. Data Cleaning with Python

Python and Pandas were used to prepare the raw dataset for analysis.

The data-cleaning process included:

- Handling missing review ratings using category-level median values
- Standardizing column names using snake_case
- Renaming the purchase amount column
- Creating age groups
- Converting purchase frequency into the number of days
- Removing the unused promotional code column
- Exporting the cleaned dataset to Excel

### 2. Data Storage with MySQL

The cleaned dataset was imported into a MySQL database for structured querying and analysis.

### 3. SQL Analysis

SQL queries were used to answer business questions related to:

- Revenue by gender
- Discount usage
- Product ratings
- Shipping behavior
- Subscription behavior
- Customer segmentation
- Product performance
- Repeat purchasing
- Revenue by age group

### 4. Power BI Dashboard

Power BI was used to create interactive visualizations and dashboards to communicate customer shopping behavior and business insights.

---

## 🔍 SQL Analysis

The project includes SQL queries covering 10 business questions.

Key analysis areas include:

- Revenue comparison by gender
- Customers using discounts while spending above average
- Top products by average review rating
- Average purchase amount by shipping type
- Subscriber vs. non-subscriber spending
- Products with the highest discount rates
- Customer segmentation based on previous purchases
- Top products within each category
- Repeat buyers and subscription behavior
- Revenue contribution by age group

---

## 📈 Key Insights

The analysis revealed several patterns in the customer shopping data:

- Male customers contributed higher total revenue than female customers.
- Express-shipping customers had a slightly higher average purchase amount than Standard-shipping customers.
- Gloves, Sandals, Boots, Hat, and Handbag were among the products with the highest average review ratings.
- Customers were segmented into New, Returning, and Loyal groups based on their previous purchases.
- Hat had the highest discount rate among the products analyzed.
- Age groups showed different levels of contribution to total revenue.
- Repeat buyers were analyzed separately to understand their relationship with subscription behavior.

---

## 📊 Dashboard Preview

The Power BI dashboard provides an interactive view of:

- Customer purchasing behavior
- Product performance
- Discount usage
- Subscription behavior
- Revenue trends
- Customer segments

> **Power BI dashboard screenshot will be added here.**

---

## 📁 Project Structure

Customer-Shopping-Behavior-Analysis/

- customer_shopping_behavior_dataset.xlsx
- customer_shopping_behavior_cleaned.xlsx
- main.py
- customer_shopping_analysis.sql
- power_bi_report.pbix
- README.md

### File Description

| File | Description |
|---|---|
| `customer_shopping_behavior_dataset.xlsx` | Original raw customer shopping dataset |
| `customer_shopping_behavior_cleaned.xlsx` | Cleaned dataset generated after Python preprocessing |
| `main.py` | Python script used for data cleaning and MySQL data loading |
| `customer_shopping_analysis.sql` | SQL queries used for business analysis |
| `power_bi_report.pbix` | Power BI dashboard |
| `README.md` | Project documentation |

---

## 💡 Conclusion

This project demonstrates an end-to-end data analytics workflow, from data cleaning and transformation to SQL-based analysis and Power BI visualization.

It combines Python, Excel, MySQL, SQL, and Power BI to transform customer shopping data into business-oriented insights.

---

## 👤 Author

**Dhruv Wakkar**

Aspiring Data Analyst | SQL | Python | Excel | Power BI

[LinkedIn](www.linkedin.com/in/dhruvwakkar)
