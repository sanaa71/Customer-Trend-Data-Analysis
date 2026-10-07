import pandas as pd
import os

# Paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "data", "customer_shopping_cleaned.csv")
excel_path = os.path.join(base_dir, "data", "customer_shopping_cleaned.xlsx")

# Load cleaned dataset
df = pd.read_csv(csv_path)

# 1. Executive KPIs
kpi_df = pd.DataFrame([
    {"Metric": "Total Revenue (USD)", "Value": f"${df['purchase_amount_usd'].sum():,.2f}"},
    {"Metric": "Total Customer Transactions", "Value": f"{len(df):,}"},
    {"Metric": "Average Order Value (AOV)", "Value": f"${df['purchase_amount_usd'].mean():,.2f}"},
    {"Metric": "Average Customer Rating", "Value": f"{df['review_rating'].mean():.2f} / 5.0"},
    {"Metric": "Subscription Adoption Rate", "Value": f"{(df['subscription_status'] == 'Yes').mean() * 100:.1f}%"},
    {"Metric": "Discount Redemption Rate", "Value": f"{(df['discount_applied'] == 'Yes').mean() * 100:.1f}%"}
])

# 2. Category Performance
cat_summary = df.groupby("category").agg(
    Total_Sales=("purchase_amount_usd", "sum"),
    Total_Orders=("purchase_amount_usd", "count"),
    Avg_Order_Value=("purchase_amount_usd", "mean"),
    Avg_Rating=("review_rating", "mean")
).sort_values(by="Total_Sales", ascending=False).reset_index()

# 3. Top 10 Products
top_items = df.groupby("item_purchased").agg(
    Total_Sales=("purchase_amount_usd", "sum"),
    Total_Orders=("purchase_amount_usd", "count"),
    Avg_Purchase_Amount=("purchase_amount_usd", "mean")
).sort_values(by="Total_Sales", ascending=False).head(10).reset_index()

# 4. Demographics
demographics = df.groupby("gender").agg(
    Total_Sales=("purchase_amount_usd", "sum"),
    Customer_Count=("customer_id", "count"),
    Avg_Spend=("purchase_amount_usd", "mean")
).reset_index()

# Export multi-tab Excel workbook
with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Cleaned_Data", index=False)
    kpi_df.to_excel(writer, sheet_name="Executive_KPIs", index=False)
    cat_summary.to_excel(writer, sheet_name="Category_Performance", index=False)
    top_items.to_excel(writer, sheet_name="Top_10_Products", index=False)
    demographics.to_excel(writer, sheet_name="Demographics", index=False)

print(f"Excel workbook successfully generated at: {excel_path}")
