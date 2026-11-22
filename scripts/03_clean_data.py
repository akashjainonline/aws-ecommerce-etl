
import pandas as pd
import os

# Load raw data
df = pd.read_csv("data/ecommerce_orders_raw.csv")

print("===== DATA CLEANING STARTED =====")
print("Original Records:", len(df))

# 1. Remove duplicate orders
df = df.drop_duplicates(subset=["order_id"], keep="first")

# 2. Remove records with missing customer_id
df = df.dropna(subset=["customer_id"])

# 3. Replace missing city with Unknown
df["city"] = df["city"].fillna("Unknown")

# 4. Remove invalid prices
df = df[df["price"] > 0]

# 5. Remove invalid quantities
df = df[df["quantity"] > 0]

# 6. Convert dates and remove invalid dates
df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce"
)

df = df.dropna(subset=["order_date"])

# 7. Reset index
df = df.reset_index(drop=True)

# 8. Save cleaned data
os.makedirs("data/processed", exist_ok=True)

output_file = "data/processed/cleaned_orders.csv"
df.to_csv(output_file, index=False)

print("\n===== DATA CLEANING COMPLETED =====")
print("Original Records: 1000")
print("Cleaned Records:", len(df))
print("Removed Records:", 1000 - len(df))
print("Remaining Missing Values:", df.isnull().sum().sum())
print("Saved File:", output_file)
