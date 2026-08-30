# Cafe Sales Data Cleaning Project

## Tech Stack

- Python
- Pandas
- PyCharm

## Project Overview

This project focuses exclusively on **data cleaning and data quality validation** using a dirty cafe sales dataset.

Unlike the other projects in my portfolio, this project does not include business analysis, SQL analysis, or data visualization.

The main objective is to take a raw and inconsistent dataset, identify data quality issues, clean the data, validate the results, and produce a reliable dataset ready for further analysis.

## Dataset

The dataset contains cafe transaction data with the following columns:

- Transaction ID
- Item
- Quantity
- Price Per Unit
- Total Spent
- Payment Method
- Location
- Transaction Date

The original dataset contains several data quality issues, including missing values, invalid placeholder values, inconsistent data types, and potentially inconsistent transaction totals.

## Data Cleaning Process

### 1. Data Inspection

The original dataset was inspected using Pandas to understand its structure and identify potential problems.

The inspection included:

- First and last rows
- Dataset dimensions
- Column names
- Data types
- Descriptive statistics
- Missing values
- Duplicate rows
- Unique values

### 2. Data Quality Assessment

The dataset was checked for:

- Missing values
- Empty strings
- Duplicate records
- Invalid placeholder values
- Unexpected values within individual columns

Values such as `ERROR` and `UNKNOWN` were identified as placeholders for unavailable or invalid data.

### 3. Data Standardization

Invalid placeholder values were standardized as missing values.

The following values were converted to `NaN`:

- `ERROR`
- `UNKNOWN`
- Empty strings
- Whitespace-only values

This allowed missing and invalid data to be handled consistently.

### 4. Data Type Conversion

Columns were converted to appropriate data types:

- `Quantity` → numeric
- `Price Per Unit` → numeric
- `Total Spent` → numeric
- `Transaction Date` → datetime

Invalid values that could not be converted were automatically treated as missing values.

### 5. Data Reconstruction

Missing `Total Spent` values were reconstructed when both `Quantity` and `Price Per Unit` were available.

The expected transaction total was calculated as:

`Quantity × Price Per Unit`

This allowed recoverable missing values to be restored instead of unnecessarily removing the affected records.

### 6. Data Validation

After cleaning, the dataset was validated to check:

- Mathematical consistency between quantity, price, and total spent
- Negative quantities
- Negative prices
- Negative transaction totals
- Remaining missing values
- Duplicate records
- Final data types
- Final dataset dimensions

The validation stage was used to ensure that the cleaning process did not introduce additional inconsistencies.

## Handling Missing Values

Missing values were not automatically removed from the dataset.

When a missing value could be reliably reconstructed from other available information, it was recovered.

When the original value could not be reliably determined, the missing value was retained as `NaN`.

This approach avoids introducing assumptions into the dataset and preserves data integrity.

## Output

The cleaned dataset is exported as:

`cleaned_cafe_sales.csv`

The final dataset is stored in the `cleaned` directory.

## Project Structure

```text
Data_cleaning/
│
├── cleaned/
│   └── cleaned_cafe_sales.csv
│
├── cleaning_cafe.py
├── dirty_cafe_sales.csv
└── README.md
