import pandas as pd
import os;

# Replace 'file1.csv' and 'file2.csv' with your actual file paths
data_dir = "data/"
file1 = 'horses.csv'
file2 = 'breeders.csv'
file_path1 = data_dir + file1
file_path2 = data_dir + file2

# Replace 'column1' and 'column2' with the actual column names you want to compare
column_name1 = 'BreederId'
column_name2 = 'id'

# Read the CSV files
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# Extract the columns to compare
column1_values = df1[column_name1].unique()
column2_values = df2[column_name2].unique()

# Find values in column1 that are not in column2
unique_to_column1 = set(column1_values) - set(column2_values)

# Display the results
print(f"Values in '{column_name1}' of '{file1}' that are not in '{column_name2}' of '{file2}':")
print(unique_to_column1)
print()

# Print the total number of unique values
print(f"Total unique values in '{column_name1}' of '{file1}' that are not in '{column_name2}' of '{file2}': {len(unique_to_column1)}")
print()

print("List:")
for value in unique_to_column1:
	print(value)
