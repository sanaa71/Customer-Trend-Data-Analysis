import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../data/shopping_behavior_updated.csv")

print("Original Dataset Shape:")
print(df.shape)

# --------------------------------------------------
# 1. Check missing values
# --------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------------------------
# 2. Check duplicate records
# --------------------------------------------------

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# --------------------------------------------------
# 3. Check data types
# --------------------------------------------------

print("\nData Types:")
print(df.dtypes)

# --------------------------------------------------
# 4. Convert column names to cleaner format
# --------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

print("\nCleaned Column Names:")
print(df.columns.tolist())

# --------------------------------------------------
# 5. Check missing values after cleaning
# --------------------------------------------------

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# --------------------------------------------------
# 6. Final dataset information
# --------------------------------------------------

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Dataset Info:")
print(df.info())

# --------------------------------------------------
# 7. Save cleaned dataset
# --------------------------------------------------

df.to_csv("../data/customer_shopping_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")

# ==================================================
# STEP 4 - EXPLORATORY DATA ANALYSIS
# ==================================================

print("\n" + "=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# --------------------------------------------------
# 1. Basic Sales Statistics
# --------------------------------------------------

print("\n--- Sales Statistics ---")

print("Total Sales:",
      df["purchase_amount_usd"].sum())

print("Average Purchase Amount:",
      df["purchase_amount_usd"].mean())

print("Minimum Purchase Amount:",
      df["purchase_amount_usd"].min())

print("Maximum Purchase Amount:",
      df["purchase_amount_usd"].max())

# --------------------------------------------------
# 2. Customer Overview
# --------------------------------------------------

print("\n--- Customer Overview ---")

print("Total Customers:",
      df["customer_id"].nunique())

print("Average Customer Age:",
      df["age"].mean())

print("\nGender Distribution:")
print(df["gender"].value_counts())

# --------------------------------------------------
# 3. Sales by Category
# --------------------------------------------------

print("\n--- Sales by Category ---")

category_sales = (
    df.groupby("category")["purchase_amount_usd"]
    .agg(["sum", "mean", "count"])
    .sort_values("sum", ascending=False)
)

print(category_sales)

# --------------------------------------------------
# 4. Top Products
# --------------------------------------------------

print("\n--- Top 10 Products ---")

top_products = (
    df.groupby("item_purchased")["purchase_amount_usd"]
    .agg(["sum", "count"])
    .sort_values("sum", ascending=False)
    .head(10)
)

print(top_products)

# --------------------------------------------------
# 5. Subscription Analysis
# --------------------------------------------------

print("\n--- Subscription Analysis ---")

subscription_analysis = (
    df.groupby("subscription_status")["purchase_amount_usd"]
    .agg(["sum", "mean", "count"])
)

print(subscription_analysis)

# --------------------------------------------------
# 6. Payment Method Analysis
# --------------------------------------------------

print("\n--- Payment Method Analysis ---")

payment_analysis = (
    df.groupby("payment_method")["purchase_amount_usd"]
    .agg(["sum", "count"])
    .sort_values("sum", ascending=False)
)

print(payment_analysis)

# --------------------------------------------------
# 7. Seasonal Analysis
# --------------------------------------------------

print("\n--- Seasonal Analysis ---")

season_analysis = (
    df.groupby("season")["purchase_amount_usd"]
    .agg(["sum", "mean", "count"])
    .sort_values("sum", ascending=False)
)

print(season_analysis)

# --------------------------------------------------
# 8. Purchase Frequency
# --------------------------------------------------

print("\n--- Purchase Frequency ---")

print(df["frequency_of_purchases"].value_counts())

# --------------------------------------------------
# 9. Customer Ratings
# --------------------------------------------------

print("\n--- Customer Ratings ---")

print("Average Rating:",
      df["review_rating"].mean())

print(
    df.groupby("category")["review_rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\nEDA completed successfully!")

# ==================================================
# STEP 5 - DATA VISUALIZATION
# ==================================================

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Create visuals folder
import os
os.makedirs("../visuals", exist_ok=True)


# --------------------------------------------------
# 1. Sales by Category
# --------------------------------------------------

category_sales = (
    df.groupby("category")["purchase_amount_usd"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales (USD)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("../visuals/sales_by_category.png")
plt.show()


# --------------------------------------------------
# 2. Sales by Season
# --------------------------------------------------

season_sales = (
    df.groupby("season")["purchase_amount_usd"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
season_sales.plot(kind="bar")

plt.title("Sales by Season")
plt.xlabel("Season")
plt.ylabel("Total Sales (USD)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("../visuals/sales_by_season.png")
plt.show()


# --------------------------------------------------
# 3. Top 10 Products
# --------------------------------------------------

top_products = (
    df.groupby("item_purchased")["purchase_amount_usd"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(9, 6))
top_products.plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales (USD)")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig("../visuals/top_10_products.png")
plt.show()


# --------------------------------------------------
# 4. Gender Distribution
# --------------------------------------------------

gender_counts = df["gender"].value_counts()

plt.figure(figsize=(6, 6))
gender_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Customer Gender Distribution")
plt.ylabel("")

plt.tight_layout()

plt.savefig("../visuals/gender_distribution.png")
plt.show()


# --------------------------------------------------
# 5. Subscription Status
# --------------------------------------------------

subscription_counts = df["subscription_status"].value_counts()

plt.figure(figsize=(6, 6))
subscription_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Subscription Status")
plt.ylabel("")

plt.tight_layout()

plt.savefig("../visuals/subscription_status.png")
plt.show()


# --------------------------------------------------
# 6. Payment Method
# --------------------------------------------------

payment_counts = df["payment_method"].value_counts()

plt.figure(figsize=(9, 5))
payment_counts.plot(kind="bar")

plt.title("Customers by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Purchases")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("../visuals/payment_methods.png")
plt.show()


# --------------------------------------------------
# 7. Average Rating by Category
# --------------------------------------------------

category_rating = (
    df.groupby("category")["review_rating"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
category_rating.plot(kind="bar")

plt.title("Average Rating by Category")
plt.xlabel("Category")
plt.ylabel("Average Rating")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("../visuals/category_ratings.png")
plt.show()


print("\nAll visualizations created successfully!")