from pathlib import Path
import pandas as pd


# ==========================
# LOAD DATASET
# ==========================

data_path = Path("../data_cleaning")

df = pd.read_csv(
    data_path / "dirty_cafe_sales.csv"
)


# ==========================
# INSPECTION
# ==========================

print("First rows:")
print(df.head())

print("\nLast rows:")
print(df.tail())

print("\nDataset information:")
print(df.info())

print("\nDescriptive statistics:")
print(df.describe())

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)


# ==========================
# DATA QUALITY CHECKS
# ==========================

# Missing values
print("\nMissing values:")
print(df.isnull().sum())


# Empty strings
print("\nEmpty strings:")
print((df == "").sum())


# Duplicates
print("\nDuplicates:")
print(df.duplicated().sum())


# Unique values
print("\nUnique values:")

for column in df.columns:
    print(f"\n{column}")
    print(
        df[column]
        .value_counts(dropna=False)
        .head(20)
    )


# ==========================
# STANDARDIZATION
# ==========================

# Replace invalid placeholder values with NaN
df = df.replace(
    ["ERROR", "UNKNOWN", ""],
    pd.NA
)

# Replace whitespace-only strings with NaN
df = df.replace(
    r"^\s*$",
    pd.NA,
    regex=True
)


# ==========================
# TYPE CONVERSION
# ==========================

df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["Price Per Unit"] = pd.to_numeric(
    df["Price Per Unit"],
    errors="coerce"
)

df["Total Spent"] = pd.to_numeric(
    df["Total Spent"],
    errors="coerce"
)

df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce"
)

print("\nData types after conversion:")
print(df.dtypes)


# ==========================
# MISSING VALUES AFTER CLEANING
# ==========================

print("\nMissing values after standardization and conversion:")
print(df.isna().sum())


# ==========================
# DATA RECONSTRUCTION
# ==========================

# Recalculate missing Total Spent values
# when Quantity and Price Per Unit are available.

calculated_total = (
    df["Quantity"] *
    df["Price Per Unit"]
)

df["Total Spent"] = df["Total Spent"].fillna(
    calculated_total
)


# ==========================
# DATA VALIDATION
# ==========================

# Check mathematical consistency
valid = (
    df["Quantity"].notna()
    & df["Price Per Unit"].notna()
    & df["Total Spent"].notna()
)

inconsistent_totals = (
    df.loc[valid, "Quantity"] *
    df.loc[valid, "Price Per Unit"]
    != df.loc[valid, "Total Spent"]
).sum()

print(
    "\nInconsistent totals:",
    inconsistent_totals
)


# Check negative values
print(
    "Negative quantities:",
    (df["Quantity"] < 0).sum()
)

print(
    "Negative prices:",
    (df["Price Per Unit"] < 0).sum()
)

print(
    "Negative totals:",
    (df["Total Spent"] < 0).sum()
)


# ==========================
# FINAL VALIDATION
# ==========================

print("\n==========================")
print("FINAL VALIDATION")
print("==========================")

print("\nFinal shape:")
print(df.shape)

print("\nFinal data types:")
print(df.dtypes)

print("\nFinal missing values:")
print(df.isna().sum())

print(
    "\nDuplicate rows:",
    df.duplicated().sum()
)


# ==========================
# SAVE CLEANED DATASET
# ==========================

cleaned_path = Path(
    "../data_cleaning/cleaned"
)

cleaned_path.mkdir(
    exist_ok=True
)

df.to_csv(
    cleaned_path / "cleaned_cafe_sales.csv",
    index=False
)

print(
    "\nCleaned dataset saved successfully."
)