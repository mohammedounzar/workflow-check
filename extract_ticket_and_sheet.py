import requests
import re

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

    print(f"Commit msg: {commit_msg}")

    ticket_nbr = re.findall(r'\bEEV2-\d+\b', commit_msg.upper().replace(' ', ''))  #  EEV2-1234  

    if ticket_nbr:
        print(f"Ticket number found: {ticket_nbr[0]}")
    else:
        raise ValueError("No valid ticket number found in commit message.")
    
    sheet_name = re.findall(r'\brelease-\d+\.\d+\.\d+\b', commit_msg.lower().replace(' ', ''))
    if sheet_name:  
        print(f"Sheet name found: {sheet_name[0]}")
    else:
        raise ValueError("No valid sheet name found in commit message.")
    
    return ticket_nbr[0], sheet_name[0]