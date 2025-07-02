import requests
import os
from dotenv import load_dotenv
import re

def extract_ticket_and_sheet(pr_number, github_token):

    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'}
    url = f'https://api.github.com/repos/moulineE/gitActionTestProject/pulls/{pr_number}/commits'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error {response.status_code}: {response.text}")

    commit_msg = data[-1]['commit']['message']

    print(f"Commit msg: {commit_msg}")

    ticket_nbr = re.findall(r'\bEEV2-\d+\b', commit_msg)
    if ticket_nbr:
        print(f"Ticket number found: {ticket_nbr[0]}")
    else:
        raise ValueError("No valid ticket number found in commit message.")
    
    sheet_name = re.findall(r'\brelease-\d+\.\d+\.\d+\b', commit_msg)
    if sheet_name:  
        print(f"Sheet name found: {sheet_name[0]}")
    else:
        raise ValueError("No valid sheet name found in commit message.")
    
    return ticket_nbr[0], sheet_name[0]