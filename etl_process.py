import pandas as pd
import os
import logging

# Input file
input_file = "../data/sales.csv"

# Output folder
output_folder = "../data/output"
os.makedirs(output_folder, exist_ok=True)

# Log file
log_file = "../data/output/etl_execution.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("ETL process started")

# Read CSV
df = pd.read_csv(input_file)

print("Original Data:")
print(df.head())

print("\nOriginal Shape:", df.shape)

logging.info(f"Original data shape: {df.shape}")

# Remove duplicate records
df = df.drop_duplicates()

# Remove completely empty rows
df = df.dropna(how="all")

logging.info(f"Cleaned data shape: {df.shape}")

# Save cleaned data
output_file = "../data/output/cleaned_sales.csv"
df.to_csv(output_file, index=False)

print("\nETL processing completed successfully!")
print("Cleaned Shape:", df.shape)
print("Output File:", output_file)

logging.info("Cleaned sales file created successfully")

# Create curated sales summary
completed_sales = df[df["status"] == "COMPLETED"].copy()

completed_sales["total_amount"] = (
    completed_sales["quantity"] * completed_sales["price"]
)

curated_summary = (
    completed_sales.groupby("category", as_index=False)["total_amount"]
    .sum()
)

curated_file = "../data/output/curated_sales_summary.csv"

curated_summary.to_csv(
    curated_file,
    index=False
)

print("\nCurated data created successfully!")
print(curated_summary)

logging.info("Curated sales summary created successfully")
logging.info("ETL process completed successfully")