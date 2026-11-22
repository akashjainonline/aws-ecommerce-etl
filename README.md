# AWS E-Commerce Data Engineering Pipeline



An end-to-end Data Engineering project using Python, Pandas, Amazon S3, Boto3, Parquet and Amazon Athena.



## Project Overview



This project demonstrates an ETL (Extract, Transform, Load) pipeline that processes raw e-commerce order data, performs data quality checks, cleans invalid records, converts the data into Parquet format, uploads the processed data to Amazon S3, and enables analytical queries using Amazon Athena.



## Architecture



```mermaid

flowchart TD

&#x20;   A\[Raw CSV Dataset] --> B\[Python and Pandas]

&#x20;   B --> C\[Data Quality Checks]

&#x20;   C --> D\[Data Cleaning]

&#x20;   D --> E\[Data Validation]

&#x20;   E --> F\[Parquet Conversion]

&#x20;   F --> G\[Amazon S3]

&#x20;   G --> H\[Amazon Athena]

&#x20;   H --> I\[SQL Analytics]

```



## Technologies Used



\- Python

\- Pandas

\- Boto3

\- AWS CLI

\- Amazon S3

\- Amazon Athena

\- Parquet

\- Git and GitHub



## Dataset



The sample e-commerce dataset contains 1,000 records and 10 columns:



\- order\_id

\- customer\_id

\- order\_date

\- product

\- category

\- quantity

\- price

\- city

\- payment\_method

\- status



## ETL Workflow



1\. Read raw CSV data using Pandas.

2\. Identify duplicates, missing values and invalid records.

3\. Clean and transform the dataset.

4\. Validate the cleaned data.

5\. Convert cleaned CSV data into Parquet format.

6\. Upload the Parquet file to Amazon S3 using Boto3.

7\. Query processed data using Amazon Athena.



## Data Quality Results



| Metric | Result |

|---|---:|

| Original Records | 1,000 |

| Duplicate Orders Removed | 1 |

| Missing Customer Records Removed | 1 |

| Invalid Prices Removed | 1 |

| Invalid Quantities Removed | 1 |

| Invalid Dates Removed | 1 |

| Final Clean Records | 995 |



Missing city values are replaced with `Unknown`.



All implemented data validation checks passed successfully.



## Amazon S3 Storage



AWS Region: `us-east-1`



S3 Bucket: `aakash-ecommerce-etl-data-2026`



Storage paths:



```text

raw/orders/ecommerce\_orders\_raw.csv

processed/orders/cleaned\_orders.parquet

athena-results/

```



## Amazon Athena Analytics



An external Parquet table named `ecommerce\_db.orders` was created in Amazon Athena.



### Total Orders and Revenue



```sql

SELECT

&#x20;   COUNT(\*) AS total\_orders,

&#x20;   SUM(quantity \* price) AS total\_revenue,

&#x20;   AVG(price) AS average\_product\_price

FROM ecommerce\_db.orders;

```



### City-wise Sales



```sql

SELECT

&#x20;   city,

&#x20;   COUNT(\*) AS total\_orders,

&#x20;   SUM(quantity \* price) AS total\_sales

FROM ecommerce\_db.orders

GROUP BY city

ORDER BY total\_sales DESC;

```



### Product-wise Sales



```sql

SELECT

&#x20;   product,

&#x20;   SUM(quantity) AS total\_quantity,

&#x20;   SUM(quantity \* price) AS total\_sales

FROM ecommerce\_db.orders

GROUP BY product

ORDER BY total\_sales DESC;

```



## Logging and Validation



The pipeline includes:

\- Local ETL logging.

\- Master pipeline execution logging.

\- Duplicate and missing-value checks.

\- Price and quantity validation.

\- Date validation.

\- Pipeline failure handling.



## How to Run



### 1. Clone the repository



```bash

git clone https://github.com/akashjainonline/aws-ecommerce-etl.git

cd aws-ecommerce-etl

```



### 2. Create a virtual environment



```bash

python -m venv venv

```



### 3. Activate environment on Windows



```powershell

.\\venv\\Scripts\\Activate.ps1

```



### 4. Install dependencies



```bash

pip install -r requirements.txt

```



### 5. Configure AWS CLI



```bash

aws configure

```



Configure your AWS credentials locally. Never upload AWS access keys or secret keys to GitHub.



### 6. Run the complete pipeline



```bash

python run\_pipeline.py

```



Ensure that your AWS IAM identity has the required permissions for the project S3 bucket.



## Project Status



Implemented:

\- Python ETL pipeline

\- Data cleaning and quality checks

\- Data validation

\- Parquet conversion

\- Amazon S3 upload

\- Amazon Athena SQL analytics

\- Local logging and master pipeline execution



Future Improvements:

\- AWS Glue integration

\- Automated scheduling

\- CloudWatch monitoring

\- CI/CD integration



## Learning Outcomes



\- Developed an end-to-end ETL pipeline.

\- Practiced real-world data cleaning and validation.

\- Worked with CSV and Parquet formats.

\- Integrated Python with AWS using Boto3.

\- Stored data in Amazon S3.

\- Performed SQL analytics using Amazon Athena.



\*\*Project:\*\* AWS E-Commerce Data Engineering Pipeline  

\*\*Role:\*\* Data Engineering Project  

\*\*Status:\*\* Core ETL pipeline and Athena analytics implemented



