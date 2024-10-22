import re

# Path to the text file
file_path = "example.txt"

# Define the regex pattern to search for (e.g., email addresses)
# This pattern matches basic email addresses like "user@example.com"
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Open the file and read its contents
with open(file_path, mode='r') as file:
    content = file.read()

# Perform regex search
matches = re.findall(email_pattern, content)

# Check if there are any matches
if matches:
    print(f"Found {len(matches)} email addresses:")
    for match in matches:
        print(match)
else:
    print("No email addresses found.")