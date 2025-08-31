# Mini Project: Data Insight Generator

import pandas as pd
import csv

# Load the dataset
df=pd.read_csv("C:/Users/abhis/Downloads/sales_data_with_missing.csv")
df


# Convert 'Price' to numeric (handle errors like 'unknown')
df['Price']=pd.to_numeric(df['Price'],errors='coerce')

# Check missing values
df.isnull()


# Replace rows where values are missing
df.fillna('Unknown')


#Change the DataType of 'Price' column 
df.Price.astype(float)


# Group by Region and calculate total Sales
df.groupby(['Region'])['Sales'].sum()


# Add a new column: TotalValue = Units * Price
df['TotalValue']=df.Units.fillna(0)*df.Price.fillna(0)
df


# Sort and display top 5 entries by TotalValue
df.sort_values(by='TotalValue',ascending=False).head(5)


# Save cleaned dataset to CSV
df.to_csv("sales_data_updated.csv")

pd.read_csv("sales_data_updated.csv")

