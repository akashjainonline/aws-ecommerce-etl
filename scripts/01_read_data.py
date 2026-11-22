
import pandas as pd

file_path = "data/ecommerce_orders_raw.csv"

df = pd.read_csv(file_path)

print("===== E-COMMERCE DATASET =====")

print("\nFirst 5 Records:")
print(df.head())

print("\nTotal Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())
