# Mini Projects & Assignment . 

## 📊 Mini Projects
---

## 📝 Assignment Comments (Data Visualization Design CS4001)

### The Decline of Arctic Sea Ice (1979–2021) #36
🔗 [View my comment](https://github.com/bsc-iitm/Data-Visualization-Design-CS4001/issues/36#issuecomment-2614490942)

### Centre’s Share in States’ Revenue Has Surged in the Last Decade #44
🔗 [View my comment](https://github.com/bsc-iitm/Data-Visualization-Design-CS4001/issues/44#issuecomment-2730362789)

### Comparison of Data Visualization Tools Using Bubble Charts #45
🔗 [View my comment](https://github.com/bsc-iitm/Data-Visualization-Design-CS4001/issues/45#issuecomment-2761899941)

### Effective visualization of data  #43
🔗 [View my comment](https://github.com/bsc-iitm/Data-Visualization-Design-CS4001/issues/43#issuecomment-2661506228)

---

# Retail Store Sales Analytics Mini-Project

This mini-project analyzes retail sales data from a Superstore dataset to generate business insights using Python. All charts are generated using `matplotlib` and `seaborn`.

---

## Dataset

Download the Superstore dataset here: [Superstore.csv](data/Superstore.csv)

---

## First 10 Rows of the Dataset

| Row ID | Order ID       | Order Date | Ship Mode | Customer ID | Customer Name | Segment | Country | City      | State | Postal Code | Region | Product ID | Category | Sub-Category | Product Name | Sales   | Quantity | Discount | Profit   |
|--------|----------------|------------|----------|-------------|---------------|---------|--------|-----------|-------|-------------|--------|------------|----------|--------------|--------------|--------|----------|----------|---------|
| 1      | CA-2016-152156 | 11/8/2016  | Second Class | CG-12520  | Claire Gute   | Consumer | US     | Henderson | KY    | 42420       | South  | FUR-BO-10001798 | Furniture | Bookcases   | Bush Somerset Collection Bookcase | 261.96 | 2        | 0        | 41.91   |
| 2      | CA-2016-152156 | 11/8/2016  | Second Class | CG-12520  | Claire Gute   | Consumer | US     | Henderson | KY    | 42420       | South  | FUR-CH-10000454 | Furniture | Chairs      | Hon Deluxe Fabric Upholstered Stacking Chairs | 731.94 | 3        | 0        | 219.58  |
| 3      | CA-2016-138688 | 6/12/2016  | Second Class | DV-13045  | Darrin Van Huff | Corporate | US  | Los Angeles | CA    | 90032       | West   | FUR-TA-10000577 | Furniture | Tables      | Bretford CR4500 Series Slim Rectangular Table | 957.58 | 5        | 0        | 90.51   |
| 4      | US-2015-108966 | 10/11/2015 | Standard Class | SO-20335  | Sean O'Donnell | Home Office | US  | Fort Lauderdale | FL | 33311       | South  | OFF-LA-10000240 | Office Supplies | Labels    | Self-Adhesive Address Labels for Typewriters | 22.37  | 2        | 0        | 2.52    |
| 5      | US-2015-108966 | 10/11/2015 | Standard Class | SO-20335  | Sean O'Donnell | Home Office | US  | Fort Lauderdale | FL | 33311       | South  | FUR-CH-10000454 | Furniture | Chairs      | Hon Deluxe Fabric Upholstered Stacking Chairs | 731.94 | 3        | 0        | 219.58  |
| 6      | US-2015-108966 | 10/11/2015 | Standard Class | SO-20335  | Sean O'Donnell | Home Office | US  | Fort Lauderdale | FL | 33311       | South  | TEC-PH-10002275 | Technology | Phones     | Plantronics CS50 Headset | 207.36 | 2        | 0        | 41.47   |
| 7      | CA-2016-161389 | 12/6/2016  | Second Class | SO-20335  | Sean O'Donnell | Consumer | US     | Los Angeles | CA    | 90032       | West   | FUR-BO-10001798 | Furniture | Bookcases  | Bush Somerset Collection Bookcase | 261.96 | 2        | 0        | 41.91   |
| 8      | CA-2016-138688 | 6/12/2016  | Second Class | DV-13045  | Darrin Van Huff | Corporate | US  | Los Angeles | CA    | 90032       | West   | FUR-TA-10000577 | Furniture | Tables      | Bretford CR4500 Series Slim Rectangular Table | 957.58 | 5        | 0        | 90.51   |
| 9      | US-2015-108966 | 10/11/2015 | Standard Class | SO-20335  | Sean O'Donnell | Home Office | US  | Fort Lauderdale | FL | 33311       | South  | OFF-LA-10000240 | Office Supplies | Labels    | Self-Adhesive Address Labels for Typewriters | 22.37  | 2        | 0        | 2.52    |
| 10     | US-2015-108966 | 10/11/2015 | Standard Class | SO-20335  | Sean O'Donnell | Home Office | US  | Fort Lauderdale | FL | 33311       | South  | FUR-CH-10000454 | Furniture | Chairs      | Hon Deluxe Fabric Upholstered Stacking Chairs | 731.94 | 3        | 0        | 219.58  |

---

## Charts (Click to Open)

- [Monthly Sales Trend](src/monthly_sales_trend.png)  
- [Top Products](charts/top_products.png)  
- [Region Sales](charts/region_sales.png)  

## Python Analysis Code

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/Superstore.csv", encoding="latin1")
print(df.head(10))

# Monthly Sales Trend
monthly_sales = df.groupby('Order Date')['Sales'].sum().head(10)
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend (First 10 rows)")
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.savefig("charts/monthly_sales_trend.png")
plt.close()

# Top Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top Products by Sales")
plt.savefig("charts/top_products.png")
plt.close()

# Region Sales
region_sales = df.groupby('Region')['Sales'].sum()
plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')
plt.title("Region Sales")
plt.savefig("charts/region_sales.png")
plt.close()

