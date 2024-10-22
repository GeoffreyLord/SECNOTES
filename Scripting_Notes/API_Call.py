import requests

# API URL for a specific GitHub repository (e.g., "requests" library repo)
api_url = "https://api.github.com/repos/psf/requests"

# Example headers (GitHub API typically requires a User-Agent header)
headers = {
    "Accept": "application/vnd.github.v3+json",  # GitHub API version
    "User-Agent": "YourAppName",  # GitHub requires a user agent string
    "Authorization": "token YOUR_GITHUB_ACCESS_TOKEN"  # Optional: Include if using authentication
}

# Make an explicit GET request with headers
response = requests.get(api_url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    repo_data = response.json()

    # Display the repository information
    print("Repository Information:")
    print(f"Name: {repo_data['name']}")
    print(f"Description: {repo_data['description']}")
    print(f"Stars: {repo_data['stargazers_count']}")
    print(f"Forks: {repo_data['forks_count']}")
    print(f"Language: {repo_data['language']}")
else:
    # Handle errors (if the request fails)
    print(f"Error: Unable to fetch data (status code: {response.status_code})")