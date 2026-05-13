import os
import pandas as pd

# Step 1 — Read raw data
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "raw", "Online Retail.xlsx")

df = pd.read_excel(file_path, nrows=10000)

# Step 2 — Check data
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("First 5 rows:")
print(df.head())
print("Null values:")
print(df.isnull().sum())

# Step 3 — Clean data

# Remove rows where Description is null
df = df.dropna(subset=['Description'])

# Fill missing CustomerID with 0
df['CustomerID'] = df['CustomerID'].fillna(0)

# Remove rows where Quantity is negative
df = df[df['Quantity'] > 0]

# Remove rows where UnitPrice is 0
df = df[df['UnitPrice'] > 0]

# Add new column TotalPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Check cleaned data
print("Cleaned Shape:", df.shape)
print("Null values after cleaning:")
print(df.isnull().sum())

# Step 4 — Save cleaned data
output_path = os.path.join(base_dir, "data", "processed", "cleaned_retail.csv")
df.to_csv(output_path, index=False)
print("Saved to processed folder!")