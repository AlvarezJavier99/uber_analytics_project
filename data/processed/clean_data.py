import pandas as pd
import zipfile
import os

# Path to your zip file
data_path = "/Users/javi/Desktop/uber_analytics_project/data/raw/uber_data.zip"

# File inside the zip you want
target_file = "Uber Data/Driver/driver_payments-0.csv"

# Open zip and load CSV
with zipfile.ZipFile(data_path, "r") as z:
    with z.open(target_file) as file:
        df = pd.read_csv(file)
# After loading data
print(df.head())
print(df.info())

print("Loaded data")
print(df.head())

# Clean columns
# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
# Timestamp conversion
df['local_timestamp'] = pd.to_datetime(df['local_timestamp'], errors='coerce')# Debug check
print("Columns:", df.columns.tolist())
print(df['local_timestamp'].dtype)
print(df['local_timestamp'].head())

#Best earning times
df['hour'] = df['local_timestamp'].dt.hour
df['day'] = df['local_timestamp'].dt.day_name()

print("Total earnings:", df['local_amount'].sum())
print("Total rows:", len(df))
print("Average amount:", df['local_amount'].mean())

print("\nBest hours:")
print(df.groupby('hour')['local_amount'].mean().sort_values(ascending=False))

print("\nBest days:")
print(df.groupby('day')['local_amount'].mean().sort_values(ascending=False))

#Earning per hour 
trips_per_hour = df.groupby('hour').size()
earnings_per_hour = df.groupby('hour')['local_amount'].sum()

dollars_per_hour = earnings_per_hour / trips_per_hour

print("\n$ per hour (better metric):")
print(dollars_per_hour.sort_values(ascending=False))

# Safe conversion
if 'local_amount' in df.columns:
    df['local_amount'] = pd.to_numeric(df['local_amount'], errors='coerce')
else:
    raise ValueError("Column 'local_amount' not found. Check your dataset.")

# Convert money column to numbers
df['local_amount'] = pd.to_numeric(df['local_amount'], errors='coerce')

# Remove bad rows
df = df.dropna(subset=['local_amount'])

# Make sure output folder exists
os.makedirs("data/scripts", exist_ok=True)

# Save clean file
df.to_csv("data/scripts/clean.csv", index=False)

# SAVE CLEAN DATA (PUT IT HERE)
df.to_csv("/Users/javi/Desktop/uber_analytics_project/data/processed/clean_uber_data.csv", index=False)

print("Saved clean file")
