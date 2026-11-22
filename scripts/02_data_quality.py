
import pandas as pd

# Load raw dataset
df = pd.read_csv("data/ecommerce_orders_raw.csv")

print("===== DATA QUALITY REPORT =====")

# 1. Total records
print("\nTotal Records:", len(df))

# 2. Duplicate orders
duplicates = df.duplicated(subset=["order_id"]).sum()
print("Duplicate Orders:", duplicates)

# 3. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Invalid prices
invalid_prices = (df["price"] <= 0).sum()
print("\nInvalid Prices:", invalid_prices)

# 5. Invalid quantities
invalid_quantities = (df["quantity"] <= 0).sum()
print("Invalid Quantities:", invalid_quantities)

# 6. Invalid dates
dates = pd.to_datetime(df["order_date"], errors="coerce")
invalid_dates = dates.isna().sum()
print("Invalid Dates:", invalid_dates)

# 7. Final summary
print("\n===== QUALITY CHECK COMPLETED =====")
