"""
File.json

{
    "users": [
        {
            "name": "Alice",
            "age": 30,
            "city": "New York"
        },
        {
            "name": "Bob",
            "age": 25,
            "city": "Los Angeles"
        },
        {
            "name": "Charlie",
            "age": 35,
            "city": "Chicago"
        }
    ]
}
"""


import json

# Path to the JSON file
json_file_path = "example.json"

# Open the JSON file and load the data
with open(json_file_path, mode='r') as file:
    data = json.load(file)

# Print the entire content of the JSON file
print("Full JSON Data:")
print(json.dumps(data, indent=4))  # Pretty-print the JSON data

# Access specific elements from the JSON
print("\nSpecific Data:")
for user in data['users']:  # Assuming the JSON has a list of users
    name = user['name']
    age = user['age']
    city = user['city']
    print(f"Name: {name}, Age: {age}, City: {city}")