
import pandas as pd
import os

# Read cleaned CSV
input_file = "data/processed/cleaned_orders.csv"
df = pd.read_csv(input_file)

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Create output directory
os.makedirs("data/processed", exist_ok=True)

# Save as Parquet
output_file = "data/processed/cleaned_orders.parquet"

df.to_parquet(output_file, engine="pyarrow", index=False)

# Verify Parquet file
parquet_df = pd.read_parquet(output_file)

print("===== PARQUET CONVERSION COMPLETED =====")
print("Total Records:", len(parquet_df))
print("Total Columns:", len(parquet_df.columns))
print("Parquet File:", output_file)
print("\nFirst 5 Records:")
print(parquet_df.head())
