# Airbnb Analysis Project

## Tech Stack

- Python
- Pandas
- MySQL
- Power BI

## Project Overview

This project analyzes the Airbnb datasets for Rome provided by Inside Airbnb: [https://insideairbnb.com/it/rome/](https://insideairbnb.com/it/rome/)

The project uses **Python (Pandas)**, **MySQL**, and **Power BI** and is divided into several stages:

### 1. Data Cleaning (Python / Pandas)

- Each dataset was inspected and cleaned using Pandas. Since not every dataset required extensive cleaning, only the necessary transformations were applied.
- The cleaned datasets were then exported as separate files (e.g., `cleaned_listings.csv`, `cleaned_calendar.csv`, and `cleaned_reviews.csv`).

### 2. Exploratory Data Analysis (Python / Pandas)

After cleaning, an Exploratory Data Analysis (EDA) was performed on each dataset to better understand its structure, identify patterns, and extract useful information for the following stages of the project.

### 3. Data Merging

- The cleaned datasets were merged into a single analytical dataset.
- The listings dataset was used as the primary table, while the calendar dataset was aggregated before merging.
- The reviews dataset was analyzed separately because it did not provide additional information useful for the analysis beyond what was already available in the listings dataset.
- The neighbourhood dataset was cleaned without further analysis because it did not provide additional information useful for the analysis.

### 4. Feature Engineering

New features were created to improve the business analysis, including:

- Price category
- Host type
- Availability rate

## Business Analysis

After the data cleaning, exploratory analysis, merging, and feature engineering stages, I performed a business-oriented analysis using both Python (Pandas) and MySQL.

### Python

Pandas was used for exploratory and preliminary business analysis, focusing on pricing, availability, neighbourhoods, room types, hosts, and correlations between numerical variables.

This stage helped identify relevant patterns and determine which metrics were most useful for the final business analysis.

### SQL

The final business analysis was performed in MySQL using the merged and feature-engineered dataset.

The analysis focused on:

- Average price by neighbourhood
- Average price by host type
- Average price by room type
- Average availability by price category
- Number of listings by neighbourhood
- Number of listings managed by each host

SQL aggregation functions such as `AVG()` and `COUNT()`, together with `GROUP BY`, `ORDER BY`, `ROUND()`, and `LIMIT`, were used to extract and compare the main business metrics.

The results of the analysis were then used as the foundation for the Power BI dashboard.

### Power BI – Limitations and Planned Geographical Analysis

During the Power BI stage, I encountered a limitation related to accessing geographical visualization features, which require a Power BI account.

For this reason, I was not able to implement the geographical analysis directly in the final dashboard.

However, the dataset contains latitude and longitude coordinates for each listing, which would allow a geographical analysis of Airbnb listings across Rome.

The planned analysis would include:

- Geographic distribution of Airbnb listings
- Listing density by area
- Average price by geographical area
- Price distribution across different areas
- Comparison of room types by location

A Power BI map visual could be used to plot the listings using latitude and longitude, with price, room type, or availability used as additional dimensions.
