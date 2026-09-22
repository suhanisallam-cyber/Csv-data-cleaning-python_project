import pandas as pd

#load the csv file
data = pd.read_csv("raw_sales_data.csv")

#display first 5rows
print(data.head())

#display number of rows and columns
print(data.shape)

#display columns name
print(data.columns)

#display basic information
print(data.info())

## Check for missing values in each column
print(data.isnull().sum())

# Display rows containing missing values
print(data[data.isnull().any(axis=1)])

# Calculate the median quantity
print(data["Quantity"].median())

# Fill missing quantity values with the median
data["Quantity"] = data["Quantity"].fillna(data["Quantity"].median())

# Verify that missing quantity values have been filled
print(data.loc[[9, 30]])

# Fill missing city values with "Unknown"
data["City"] = data["City"].fillna("Unknown")

# Check missing values after filling City
print(data.isnull().sum())

# Check for duplicate rows
print(data.duplicated().sum())

# Display duplicate rows
print(data[data.duplicated()])

# Remove duplicate rows
data = data.drop_duplicates()

# Check the number of duplicate rows after cleaning
print(data.duplicated().sum())

# Check for negative unit prices
print(data[data["Unit_Price"] < 0])

# Correct negative unit prices
data.loc[data["Unit_Price"] < 0, "Unit_Price"] = 700

# Check for negative unit prices after cleaning
print(data[data["Unit_Price"] < 0])

# Display unique category values
print(data["Category"].unique())

# Standardize category names
data["Category"] = data["Category"].str.title()

# Standardize category names
data["Category"] = data["Category"].str.title()

# Check category values after standardization
print(data["Category"].unique())

# Check the data types of all columns
print(data.dtypes)

# Convert Order_Date to datetime format
data["Order_Date"] = pd.to_datetime(data["Order_Date"])

# Check the data types after conversion
print(data.dtypes)

# Perform a final data quality check to ensure the dataset is clean

# Check for remaining missing values
print(data.isnull().sum())

# Check for duplicate rows
print("Duplicate rows:", data.duplicated().sum())

# Check for negative prices
print("Negative prices:", (data["Unit_Price"] < 0).sum())

# Check unique categories
print("Categories:", data["Category"].unique())

# Save the cleaned data to a new CSV file
data.to_csv("cleaned_sales_data.csv", index=False)

print("Data cleaning completed successfully!")





