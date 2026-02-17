import pandas as pd

df = pd.read_csv("cleaned_sales_data.csv")

# Total Sales
total_sales = df["Sales"].sum()

# Total Profit
total_profit = df["Profit"].sum()

# Monthly Trend
monthly_trend = df.groupby("Month")["Sales"].sum()

# Top 5 products
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

print("\nMonthly Trend:\n", monthly_trend)

print("\nTop Products:\n", top_products)
