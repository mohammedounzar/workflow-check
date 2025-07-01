import requests
import os
from dotenv import load_dotenv

def extract_ticket_and_sheet(pr_number):
    load_dotenv()
    repo_name = os.getenv("REPO_NAME")
    repo_owner = os.getenv("REPO_OWNER")
    github_token = os.getenv("GITHUB_TOKEN")

    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'}
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/commits'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error {response.status_code}: {response.text}")

    commit_message = data[0]['items']['commit']['message']['examples'] 
    print(f"Commit message: {commit_message}")