
import boto3
import os

# AWS S3 configuration
bucket_name = "aakash-ecommerce-etl-data-2026"

local_file = "data/processed/cleaned_orders.parquet"

s3_key = "processed/orders/cleaned_orders.parquet"

# Check local file
if not os.path.exists(local_file):
    raise FileNotFoundError(f"File not found: {local_file}")

# Connect to S3
s3 = boto3.client("s3", region_name="us-east-1")

try:
    # Upload file to S3
    s3.upload_file(
        local_file,
        bucket_name,
        s3_key
    )

    print("===== S3 UPLOAD SUCCESSFUL =====")
    print("Bucket:", bucket_name)
    print("S3 File:", s3_key)

    # Verify uploaded file
    response = s3.head_object(
        Bucket=bucket_name,
        Key=s3_key
    )

    print("File Size:", response["ContentLength"], "bytes")
    print("Verification: File exists in S3")

except Exception as e:
    print("===== S3 UPLOAD FAILED =====")
    print("Error:", e)
