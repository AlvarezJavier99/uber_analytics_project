#======================================================================
# Uber Analytics Project - Data Cleaning Script
# Author: Javier Alvarez 
# Purpose: Clean the raw Uber data to create business insights
#======================================================================

#======================================================================
# 1. Importing Libraries
#======================================================================

import pandas as pd
import numpy as np
from pathlib import Path

#======================================================================
# 2. Loading the Data
#======================================================================

RAW_DATA_PATH = Path("C:/Users/User/Desktop/uber_analytics_project/data/raw/uber_raw_data.csv")
print(RAW_DATA_PATH)
df = pd.read_csv(RAW_DATA_PATH)

#======================================================================
# 3. Initial Data Exploration
#======================================================================

print("\n================ FIRST 5 ROWS ================\n")
print(df.head())
print("\n================ DATASET SHAPE ================\n")
print(df.shape)
print("\n================ DATA COLUMNS ================\n")
print(df.columns.tolist())
print("\n================ DATA INFO ================\n")
print(df.info())
print("\n================ MISSING VALUES ================\n")
print(df.isnull().sum())
print("\n================ WHAT ARE THE MISSING VALUES? ================\n")
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]
if missing_values.empty:
    print("No missing values found in the dataset.")
else:
    print(missing_values.sort_values(ascending=False))

#======================================================================
# 4. Data Cleaning Steps
# =====================================================================

# 4.1 Keeping only completed rides 
print("\n================ FILTERING FOR COMPLETED RIDES ================\n")
df = df[df["is_completed"] == True]
print("After filtering for only completed rides:", df.shape)

# 4.2 Removing all "local" columns that are not needed for analysis
df = df.loc[:, ~df.columns.str.endswith("_local")]
print("\n================ COLUMNS AFTER REMOVING LOCAL ================\n")
print(df.columns.tolist())
print("\nAfter removing local columns:", df.shape)

# 4.3 Removing invalid entries (negative fare amounts, zero distance)
# Storing the original dataset before removing invalid entries
original_dataset = len(df)
# Applying the filter to remove invalid entries
df = df[
    (df["trip_distance_miles"] > 0) &
    (df["trip_duration_seconds"] > 0) &
    (df["base_fare_usd"] > 0) &
    (df["original_fare_usd"] > 0) &
    (df["surge_fare_usd"] >= 0) &  # Surge fare can be zero but not negative
    (df["per_mile_fare_usd"] > 0) &
    (df["per_minute_fare_usd"] > 0) &
    (df["is_flat_rate"] >= 0) & # Flat rate can be zero but not negative
    (df["promotion_usd"] >= 0) &  # Promotion can be zero but not negative
    (df["driver_upfront_fare_usd"] >= 0) &  # Driver upfront fare can be zero but not negative
    (df["fare_distance_miles"] > 0) &
    (df["fare_duration_minutes"] > 0) ]

print("\n================ INVALID ENTRIES REMOVED ================\n")
# Store the number of invalid entries removed
invalid_entries_removed = len(df)
#Removal percentage calculation
removal_percentage = (invalid_entries_removed / original_dataset) * 100
# Print the number of invalid entries removed
print(f"Original dataset size: {original_dataset}")
print(f"Number of invalid entries removed: {original_dataset - invalid_entries_removed}")
print(f"Removal percentage: {removal_percentage:.2f}%")
print(f"Original dataset size after removing invalid entries: {df.shape[0]}")

# 4.4 Removing duplicates
print("\n================ REMOVING DUPLICATES ================\n")
rows_before_duplicates = len(df)
df = df.drop_duplicates()
rows_after_duplicates = len(df)
duplicates_removed = (rows_before_duplicates - rows_after_duplicates)
print(f"Duplicate rows removed: {duplicates_removed:,}")
print("Updated dataset shape:", df.shape)

# 4.5 Correcting time format and extracting day of week and hour of day for analysis
# Convert the 'begintrip_timestamp_utc' column to datetime format
df["begintrip_timestamp_utc"] = pd.to_datetime(df["begintrip_timestamp_utc"])
# Create day name column and hour column for analysis
df["pickup_day"] = df["begintrip_timestamp_utc"].dt.day_name()
df["pickup_hour"] = df["begintrip_timestamp_utc"].dt.hour
df["pickup_month"] = df["begintrip_timestamp_utc"].dt.month_name()
print("\n================ TIMESTAMP COLUMNS CREATED ================\n")
print(df[["begintrip_timestamp_utc", "pickup_day", "pickup_hour", "pickup_month"]].head())

# ===================================================================
# 5. Key Performance Indicators (KPIs) Metrics 
# ===================================================================

print("\n================ CALCULATING KPI METRICS ================\n")
# 5.1 Revenue per Mile
df["revenue_per_mile"] = df["original_fare_usd"] / df["trip_distance_miles"]

# 5.2 Revenue per Hour
df["revenue_per_hour"] = (df["original_fare_usd"] / (df["trip_duration_seconds"] / 3600))
print(df[[
    "original_fare_usd",
    "revenue_per_hour",
    "begintrip_timestamp_utc",
]].head())
#====================================================================================================
###### PAUSE POINT - I WAS IN THE PROCESS OF CALACUTING THE MOST ACRUTE WAY TO DETERMINE COST PER MILE AND ABERAGE MILES DRIVEN A DAY 