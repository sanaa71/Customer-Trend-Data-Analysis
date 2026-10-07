# Customer Trend Data Analysis 📊🛒

An end-to-end data analytics project exploring customer shopping behavior, purchasing patterns, demographics, and product performance. The project utilizes **Excel**, **Python (Pandas, NumPy)**, **SQL**, and **Power BI** to deliver actionable insights and executive dashboards.

---

## 📌 Executive Summary

This project analyzes a customer shopping dataset containing **3,900 customer transaction records across 18 behavioral attributes** to identify purchasing patterns, product performance, customer demographics, seasonal trends, and payment preferences.

### Key Metrics

* **Dataset Size:** 3,900 customer transaction records
* **Total Revenue Analyzed:** $233,081 USD
* **Average Order Value:** $59.76
* **Product Range:** 25 unique items across 4 categories
* **Average Review Rating:** 3.75 / 5

### Tech Stack

* **Data Cleaning & Analysis:** Python, Pandas, NumPy
* **Data Visualization:** Matplotlib
* **Database:** MySQL 8.0
* **Business Intelligence:** Power BI
* **Spreadsheet Analysis:** Excel
* **Version Control:** Git & GitHub

---

## 🎯 Project Objectives

* Analyze customer shopping and purchasing behavior
* Identify high-performing product categories and products
* Analyze sales trends across seasons and customer demographics
* Understand payment, shipping, subscription, discount, and promotional patterns
* Analyze customer purchase frequency and previous purchase behavior
* Build interactive dashboards for business decision-making
* Transform raw customer data into actionable business insights

---

## 🧹 Data Engineering & Cleaning

The raw customer shopping dataset was cleaned and preprocessed using **Python/Pandas**.

Key data preparation tasks included:

* Standardizing column names
* Checking and handling missing values
* Validating data types
* Checking duplicate records
* Cleaning categorical values
* Preparing the dataset for SQL and Power BI analysis
* Exporting the cleaned dataset for downstream analysis

The final dataset contains **3,900 records and 18 attributes**.

---

## 🔍 Exploratory Data Analysis & SQL

Performed exploratory analysis using **Python, Pandas, NumPy, and Matplotlib** to understand customer purchasing patterns and sales performance.

Developed **15+ SQL business analysis queries using MySQL 8.0**, covering:

1. Total sales
2. Average purchase amount
3. Sales by category
4. Top 10 products by sales
5. Sales by gender
6. Subscription analysis
7. Sales by season
8. Payment method analysis
9. Average rating by category
10. Sales by location
11. Discount impact
12. Promo code analysis
13. Purchase frequency
14. Shipping type analysis
15. Previous purchase behavior

---

## 📊 Power BI Dashboard

Developed a **3-page interactive Power BI dashboard** to present key business insights.

### Page 1 — Sales Overview

Includes:

* Total Sales KPI
* Average Purchase KPI
* Total Customers KPI
* Sales by Category
* Sales by Season
* Top 10 Products by Sales
* Sales by Gender
* Sales by Subscription Status
* Interactive Category, Season, and Gender slicers

### Page 2 — Customer & Payment Analysis

Includes:

* Sales by Payment Method
* Top 10 Locations by Sales
* Sales by Purchase Frequency
* Average Rating by Category
* Sales by Discount Status
* Sales by Promo Code Usage
* Sales by Shipping Type
* Previous Purchase History
* Interactive Category, Season, and Gender slicers

### Page 3 — Product Analysis

Includes:

* Product Sales by Category
* Top 10 Products by Sales
* Average Rating by Product
* Average Rating by Category
* Sales Distribution by Category
* Sales by Product Size
* Sales by Product Color
* Category Sales by Season
* Interactive Category, Season, and Size slicers

---

## 📈 Excel Analysis

Excel was used as an additional tool for data inspection and analysis where applicable.

The analysis can be organized into:

* **Cleaned_Data**
* **Executive_KPIs**
* **Category_Performance**
* **Top_10_Products**
* **Demographics**

---

## 📊 Visualizations & Key Findings

The project includes visualizations covering:

* Sales by Category
* Sales by Season
* Top 10 Products
* Gender Distribution
* Subscription Status
* Payment Methods
* Category Ratings

### Key Findings

* **Clothing** generated the highest category sales at approximately **$104K**.
* **Fall** recorded the highest seasonal sales at approximately **$60K**.
* **Blouse, Shirt, and Dress** were among the highest-selling products.
* Sales were relatively balanced across the analyzed payment methods.
* Subscription customers accounted for approximately **$62.6K** in sales.
* The overall average review rating was approximately **3.75 / 5**.
* **Footwear** recorded the highest average rating among the four product categories.

---

## 📁 Repository Structure

```text
Customer-Trend-Data-Analysis/
│
├── data/
│   ├── shopping_behavior_updated.csv
│   └── customer_shopping_cleaned.csv
│
├── python/
│   └── analysis.py
│
├── sql/
│   └── customer_analysis.sql
│
├── visuals/
│   ├── category_ratings.png
│   ├── gender_distribution.png
│   ├── payment_methods.png
│   ├── sales_by_category.png
│   ├── sales_by_season.png
│   ├── subscription_status.png
│   └── top_10_products.png
│
├── powerbi/
│   └── Customer_Trend_Data_Analysis.pbix
│
└── README.md
```

---

## 💼 ATS-Friendly Project Highlights

### Data Engineering & Cleaning

* Cleaned, preprocessed, and validated **3,900+ customer records** using Python/Pandas, preparing structured data for SQL and Power BI analysis.

### EDA & SQL

* Performed exploratory data analysis and developed **15+ SQL business queries** using MySQL to analyze sales, products, demographics, subscriptions, discounts, payments, and purchasing behavior.

### Business Intelligence

* Built a **3-page interactive Power BI dashboard** with KPIs, slicers, and visualizations to communicate sales, customer, payment, and product insights.

---

## 🛠️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/sanaa71/Customer-Trend-Data-Analysis.git
cd Customer-Trend-Data-Analysis
```

### 2. Install Python dependencies

```bash
pip install pandas numpy matplotlib
```

### 3. Run Python analysis

```bash
python python/analysis.py
```

### 4. SQL Analysis

Open **MySQL 8.0** and execute the queries in:

```text
sql/customer_analysis.sql
```

### 5. Power BI Dashboard

Open:

```text
powerbi/Customer_Trend_Data_Analysis.pbix
```

---

## 🎯 Business Value

This project demonstrates an end-to-end data analytics workflow:

**Raw Data → Data Cleaning → Exploratory Analysis → SQL Business Analysis → Power BI Visualization → Business Insights**

The analysis provides insights into product performance, customer demographics, seasonal sales, payment preferences, subscription activity, promotional behavior, and purchasing patterns.

---

## 👩‍💻 Author

"Sanaa Shaikh"

Final-Year Computer Science Engineering Student
Aspiring Data Analyst / Business Analyst/Data Scientist

---

⭐ If you find this project useful, feel free to explore the repository and dashboards.
