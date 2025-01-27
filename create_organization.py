import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
ORG_NAME = 'shashashazize'  # Your organization name
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def create_repository(repo_name):
    url = f'https://api.github.com/orgs/{ORG_NAME}/repos'
    data = {
        'name': repo_name,
        'private': False
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f'Repository {repo_name} created successfully.')
    else:
        print(f'Failed to create repository {repo_name}: {response.json()}')

# Create 10 repositories
for i in range(1, 11):
    create_repository(f'repo{i}')