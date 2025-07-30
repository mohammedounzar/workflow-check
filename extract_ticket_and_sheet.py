import requests
from parse_commit_message import parse_commit_message

def extract_ticket_and_sheet(pr_number, github_token, repo_name, repo_owner):
        headers = {
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github.v3+json'}
        url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/commits?per_page=100'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Error {response.status_code}: {response.text}")

        commit_msg = data[-1]['commit']['message']  # [release-1.2.3] EEV2-1234

        print(f"Commit msg: {commit_msg}")    #  EE2 - 72727    

        ticket_nbr, sheet_name = parse_commit_message(commit_msg)

        return ticket_nbr, sheet_name