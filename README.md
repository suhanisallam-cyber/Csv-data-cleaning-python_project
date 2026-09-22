# Sales Data Cleaning using Python

##  Project Overview
This project focuses on cleaning and preprocessing a raw sales dataset using Python and Pandas.
The dataset contains common data quality issues such as missing values, duplicate records, negative prices, inconsistent category names,
and date formatting issues.
The main goal of this project is to transform raw and inconsistent data into a clean and analysis-ready dataset.

## Technologies Used
- Python
- Pandas
- CSV

## Data Cleaning Steps
The following data cleaning operations were performed:

1. Checked the dataset structure and data types.
2. Identified missing values.
3. Filled missing Quantity values using the median.
4. Filled missing City values with "Unknown".
5. Identified and removed duplicate records.
6. Checked for negative Unit_Price values and corrected the practice dataset.
7. Standardized Category names.
8. Converted Order_Date into datetime format.
9. Performed a final data quality check.
10. Saved the cleaned dataset as a new CSV file.

##  Data Quality Checks
The following checks were performed:

- Missing values
- Duplicate rows
- Negative prices
- Inconsistent category names
- Incorrect data types

##  Project Objective
The objective of this project is to understand the basic process of data cleaning using Python and Pandas and prepare raw data for further analysis.

##  Key Learnings
Through this project, I learned how to:

- Load CSV data using Pandas
- Identify missing values
- Handle missing data
- Remove duplicate records
- Detect data quality issues
- Standardize text values
- Convert columns to appropriate data types
- Export cleaned data to a CSV file
