import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("C:/Users/User/Desktop/uber_analytics_project/data/raw/uber_raw_data.csv")
print(RAW_DATA_PATH)
df = pd.read_csv(RAW_DATA_PATH)
print(df.head())
print(df.shape)
print(df.columns.tolist())
df = df[df["is_completed"] == True]
print("After filtering:", df.shape)
