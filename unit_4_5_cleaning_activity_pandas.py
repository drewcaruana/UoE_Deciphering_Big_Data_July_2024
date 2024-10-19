# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:30:35 2024

@author: Andrew Caruana
"""
# Importing packages
import pandas as pd
import matplotlib.pyplot as plt

# File paths - Please enter file paths between inverted commas
survey_file = r""
survey_headers_file = r""
updated_survey_headers_file = r""

# Load the data
data_df = pd.read_csv(survey_file, encoding='utf-8')
headers_df = pd.read_csv(updated_survey_headers_file, encoding='utf-8')

# Ensure only columns present in the header file are kept in the data
filtered_headers = headers_df[headers_df['Name'].isin(data_df.columns)]

# Keep only the relevant columns in the data
data_df = data_df[filtered_headers['Name']]

# Check for header mismatches (matching between filtered headers and data columns)
header_match = list(zip(data_df.columns, filtered_headers['Name']))
print(header_match)

# Displaying questions and answers for the first row
first_row = data_df.iloc[0]
for col, description, label in zip(first_row.index, filtered_headers['Question'], filtered_headers['Label']):
    
    # Use the column description if it's not empty, otherwise use the label column
    question = description if pd.notna(description) and description.strip() else label
    print(f'Question: {question}\nAnswer: {first_row[col]}')

# Look for missing data across all rows
missing_data = data_df.isnull().sum().sum()

# Print total points of missing data
if missing_data > 0:
    print(f"Total missing data points: {missing_data}")
    
    # Print rows were missing data is found
    missing_data_details = data_df.isnull().stack()
    for index in missing_data_details[missing_data_details].index:
        question = filtered_headers[filtered_headers['Name'] == index[1]]['Question'].values[0]
        # print(f"Missing data in row {index[0] + 1}, question '{question}' (code: {index[1]})")

# Look for duplicates
duplicates = data_df.duplicated(keep=False)
if duplicates.any():
    print(f"Total duplicates found: {duplicates.sum()}")
    duplicate_rows = data_df[duplicates]
    print(f"Duplicate rows:\n{duplicate_rows}")
else:
    print("No duplicates found.")

# Adding visualisation of missing values to identify variables with the highest missing values
# Calculate the percentage of missing values per column
missing_values_per_column = data_df.isnull().mean() * 100

# Plot the columns that have over 60% missing values
plt.figure(figsize=(10, 6))
missing_values_per_column[missing_values_per_column > 60].plot(kind='bar', color='skyblue')
plt.title('Percentage of Missing Values Per Column')
plt.xlabel('Columns')
plt.ylabel('Percentage of Missing Values (%)')
plt.xticks(rotation=90)
plt.tight_layout()

# Show the plot
plt.show()