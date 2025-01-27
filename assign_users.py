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


def add_collaborator(repo_name, username, permission):
    url = f'https://api.github.com/repos/{ORG_NAME}/{repo_name}/collaborators/{username}'
    data = {
        'permission': permission
    }
    response = requests.put(url, headers=HEADERS, json=data)
    if response.status_code in [201, 204]:
        print(f'User {username} added to {repo_name} with {permission} permission.')
    else:
        print(f'Failed to add user {username} to {repo_name}: {response.json()}')


# Assign collaborators
assignments = {
    'repo1': 'Maxxbw54',
    'repo2': 'zeshili',
    'repo3': 'Maxxbw54',
    'repo4': 'zeshili',
    'repo5': 'Maxxbw54',
    'repo6': 'zeshili',
    'repo7': 'Maxxbw54',
    'repo8': 'zeshili',
    'repo9': 'Maxxbw54',
    'repo10': 'zeshili'
}

for repo, user in assignments.items():
    add_collaborator(repo, user, 'write')  # Change permission as needed