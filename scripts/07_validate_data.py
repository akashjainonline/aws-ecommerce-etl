
import pandas as pd
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "processed" / "cleaned_orders.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

def validate_data(df):

    errors = []

    # 1. Required columns
    required_columns = [
        "order_id", "customer_id", "order_date",
        "product", "category", "quantity",
        "price", "city", "payment_method", "status"
    ]

    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        errors.append(f"Missing columns: {missing_columns}")
    else:
        logging.info("PASS: All required columns exist")

    if missing_columns:
        return errors

    # 2. Missing values
    if df[required_columns].isnull().any().any():
        errors.append("Missing values found")
    else:
        logging.info("PASS: No missing values")

    # 3. Duplicate orders
    if df["order_id"].duplicated().any():
        errors.append("Duplicate order IDs found")
    else:
        logging.info("PASS: No duplicate orders")

    # 4. Invalid price and quantity
    if (df["price"] <= 0).any():
        errors.append("Invalid prices found")
    else:
        logging.info("PASS: All prices are positive")

    if (df["quantity"] <= 0).any():
        errors.append("Invalid quantities found")
    else:
        logging.info("PASS: All quantities are positive")

    # 5. Valid order dates
    dates = pd.to_datetime(df["order_date"], errors="coerce")

    if dates.isnull().any():
        errors.append("Invalid order dates found")
    else:
        logging.info("PASS: All order dates are valid")

    return errors


try:
    logging.info("Data validation started")

    df = pd.read_csv(input_file)

    logging.info(f"Records loaded: {len(df)}")

    validation_errors = validate_data(df)

    if validation_errors:
        logging.error("DATA VALIDATION FAILED")

        for error in validation_errors:
            logging.error(error)

        raise ValueError("Data quality checks failed")

    logging.info("DATA VALIDATION PASSED")
    logging.info("All data quality checks completed successfully")

except Exception:
    logging.exception("Validation process failed")
    raise
