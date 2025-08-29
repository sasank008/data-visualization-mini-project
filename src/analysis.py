import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load only first 10 rows
df = pd.read_csv("data/Superstore.csv", encoding="latin1", nrows=10)

print("CSV loaded successfully! First 10 rows:")
print(df.head(10))

# Example chart 1: Monthly Sales Trend
monthly_sales = df.groupby('Order Date')['Sales'].sum()
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend (First 10 rows)")
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

# Create 'charts' folder if it doesn't exist
import os
os.makedirs("charts", exist_ok=True)

plt.savefig("charts/monthly_sales_trend.png")
plt.close()
print("Monthly Sales Trend chart saved!")

# Example chart 2: Top Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top Products (First 10 rows)")
plt.xlabel("Sales")
plt.ylabel("Product Name")
plt.tight_layout()
plt.savefig("charts/top_products.png")
plt.close()
print("Top Products chart saved!")

# Example chart 3: Region Sales
region_sales = df.groupby('Region')['Sales'].sum()
plt.figure(figsize=(7,5))
region_sales.plot(kind='bar', color='skyblue')
plt.title("Region Sales (First 10 rows)")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/region_sales.png")
plt.close()
print("Region Sales chart saved!")

print("All analysis done successfully!")
