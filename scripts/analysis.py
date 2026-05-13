import os
import pandas as pd

# Read cleaned data
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "processed", "cleaned_retail.csv")
df = pd.read_csv(file_path)

# 1 — Total revenue
print("Total Revenue:", df['TotalPrice'].sum())

# 2 — Top 5 countries by revenue
print("\nTop 5 Countries:")
print(df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head())

# 3 — Top 5 best selling products
print("\nTop 5 Products:")
print(df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head())

# 4 — Total orders per country
print("\nOrders per Country:")
print(df.groupby('Country')['InvoiceNo'].nunique().sort_values(ascending=False).head())