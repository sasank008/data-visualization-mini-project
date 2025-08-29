# src/analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Absolute path to your CSV file
csv_path = r"C:\Users\sasank moulidhar\Downloads\retail-sales-analytics\data\Superstore.csv"

# Check if the file exists
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV file not found at {csv_path}")

# Read CSV
df = pd.read_csv(csv_path, encoding="latin1")

# Quick check
print("CSV loaded successfully! First 5 rows:")
print(df.head())

# --- Example Analysis 1: Monthly Sales Trend ---
df['Order Date'] = pd.to_datetime(df['Order Date'])
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()

plt.figure(figsize=(12,6))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\sasank moulidhar\Downloads\retail-sales-analytics\monthly_sales_trend.png")
plt.close()
print("Monthly Sales Trend chart saved!")

# --- Example Analysis 2: Top 10 Products by Sales ---
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(r"C:\Users\sasank moulidhar\Downloads\retail-sales-analytics\top_products.png")
plt.close()
print("Top Products chart saved!")

# --- Example Analysis 3: Sales by Region ---
region_sales = df.groupby('Region')['Sales'].sum()
plt.figure(figsize=(8,6))
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig(r"C:\Users\sasank moulidhar\Downloads\retail-sales-analytics\region_sales.png")
plt.close()
print("Region Sales chart saved!")

print("All analysis done successfully!")

# Save charts in charts/ folder
plt.savefig("../charts/monthly_sales_trend.png")
plt.savefig("../charts/top_products.png")
plt.savefig("../charts/region_sales.png")


