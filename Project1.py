from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent

print("Script file location:")
print(PROJECT_ROOT)

RAW_DIR = PROJECT_ROOT / "Raw_Data" / "df.csv"
print("Raw Data Path is:")
print(RAW_DIR)
df = pd.read_csv(RAW_DIR)
print(df)

