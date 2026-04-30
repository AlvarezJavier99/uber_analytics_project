import pandas as pd
import zipfile
import os

# Path to your zip file
data_path = "data/raw/uber_data.zip"

# File inside the zip you want
target_file = "Uber Data/Driver/driver_payments-0.csv"

# Open zip and load CSV
with zipfile.ZipFile(data_path, "r") as z:
    with z.open(target_file) as file:
        df = pd.read_csv(file)

print("Loaded data")
print(df.head())

# Clean columns
df.columns = df.columns.str.lower().str.strip()

# Convert money column to numbers
df['local_amount'] = pd.to_numeric(df['local_amount'], errors='coerce')

# Remove bad rows
df = df.dropna(subset=['local_amount'])

# Make sure output folder exists
os.makedirs("data/processed", exist_ok=True)

# Save clean file
df.to_csv("data/processed/clean.csv", index=False)

print("Saved clean file")

## Just cheking to push to GitHub, ignore this part.