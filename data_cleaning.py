import pandas as pd

df = pd.read_csv("sales_data.csv")

# Remove missing values
df = df.dropna()

# Convert date column to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Add Year & Month column
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

df.to_csv("cleaned_sales_data.csv", index=False)

print("Data cleaning complete!")
