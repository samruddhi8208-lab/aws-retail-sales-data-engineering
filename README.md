# aws-retail-sales-data-engineering
AWS Data Engineering project using S3, Glue, Lambda, RDS, EMR and Redshift
## Project Overview

This project demonstrates an end-to-end retail sales data engineering pipeline using AWS and Python.

## Architecture

S3 Raw Data
↓
AWS Lambda
↓
ETL Processing
↓
S3 Processed Data
↓
S3 Curated Data
↓
Analytics Ready Data

## AWS Services Used

- Amazon S3
- AWS Lambda
- AWS IAM
- AWS Glue Database
- Amazon CloudWatch

## Technologies Used

- Python
- Pandas
- CSV
- AWS
- PyCharm
- GitHub

## S3 Data Layers

### Raw Layer
Original sales data stored in S3.

File: `sales.csv`

### Processed Layer
Cleaned sales data generated after ETL processing.

File: `cleaned_sales.csv`

### Curated Layer
Analytics-ready category-wise sales summary.

File: `curated_sales_summary.csv`

### Scripts Layer
Contains the ETL script.

File: `etl_process.py`

### Logs Layer
Contains ETL execution logs.

File: `etl_execution.log`

## ETL Process

1. Read raw sales CSV.
2. Remove duplicate records.
3. Remove completely empty rows.
4. Generate cleaned sales data.
5. Filter completed orders.
6. Calculate total sales amount.
7. Generate category-wise sales summary.
8. Generate ETL execution logs.

## AWS Lambda

An S3 trigger invokes the Lambda function when a new file is uploaded to the `raw/` folder.

## Project Outcome

The project creates separate raw, processed, curated, scripts, and logs layers and demonstrates a practical cloud-based ETL workflow.
