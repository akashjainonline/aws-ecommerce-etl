
import pandas as pd
import logging
from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(
            LOG_DIR / "etl_pipeline.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ],
    force=True
)

try:
    logging.info("ETL pipeline started")

    # Read raw data
    input_file = BASE_DIR / "data" / "ecommerce_orders_raw.csv"
    df = pd.read_csv(input_file)

    original_count = len(df)
    logging.info(f"Raw records loaded: {original_count}")

    # Remove duplicate orders
    duplicates = df.duplicated(subset=["order_id"]).sum()
    df = df.drop_duplicates(subset=["order_id"], keep="first")
    logging.info(f"Duplicate records removed: {duplicates}")

    # Remove missing customer IDs
    missing_customers = df["customer_id"].isna().sum()
    df = df.dropna(subset=["customer_id"])
    logging.info(f"Missing customer records removed: {missing_customers}")

    # Handle missing cities
    missing_cities = df["city"].isna().sum()
    df["city"] = df["city"].fillna("Unknown")
    logging.info(f"Missing cities replaced: {missing_cities}")

    # Remove invalid prices
    invalid_prices = (df["price"] <= 0).sum()
    df = df[df["price"] > 0]
    logging.info(f"Invalid prices removed: {invalid_prices}")

    # Remove invalid quantities
    invalid_quantities = (df["quantity"] <= 0).sum()
    df = df[df["quantity"] > 0]
    logging.info(f"Invalid quantities removed: {invalid_quantities}")

    # Convert dates and remove invalid dates
    df["order_date"] = pd.to_datetime(
        df["order_date"], errors="coerce"
    )

    invalid_dates = df["order_date"].isna().sum()
    df = df.dropna(subset=["order_date"])
    logging.info(f"Invalid dates removed: {invalid_dates}")

    # Save cleaned data
    output_dir = BASE_DIR / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "cleaned_orders.csv"
    df.to_csv(output_file, index=False)

    logging.info(f"Cleaned records: {len(df)}")
    logging.info(f"Records removed: {original_count - len(df)}")
    logging.info(f"Output saved: {output_file}")
    logging.info("ETL pipeline completed successfully")

except Exception:
    logging.exception("ETL pipeline failed")
    raise
