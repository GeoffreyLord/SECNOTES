"""
File.csv
Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
"""

import csv

# Path to the CSV file
csv_file_path = "example.csv"

# Open the CSV file and create a CSV reader object
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Read the header row
    header = next(csv_reader)
    print(f"Header: {header}")
    
    # Iterate through the rows in the CSV
    for row in csv_reader:
        # Print each row (or process it as needed)
        print(f"Row: {row}")
        
        # Access specific columns (assuming CSV has columns like 'Name', 'Age', 'City')
        name = row[0]  # First column (e.g., Name)
        age = row[1]   # Second column (e.g., Age)
        city = row[2]  # Third column (e.g., City)

        print(f"Name: {name}, Age: {age}, City: {city}")