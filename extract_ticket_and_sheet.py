import requests
import re
from parse_commit_message import CommitMessageParser


class TicketAndSheetExtractor:
    def __init(self, pr_number, github_token, repo_name, repo_owner):
        self.pr_number = pr_number
        self.github_token = github_token
        self.repo_name = repo_name
        self.repo_owner = repo_owner

    def extract_ticket_and_sheet(self):
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'}
        url = f'https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/pulls/{self.pr_number}/commits?per_page=100'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Error {response.status_code}: {response.text}")

        commit_msg = data[-1]['commit']['message']  # [release-1.2.3] EEV2-1234

        print(f"Commit msg: {commit_msg}")    #  EE2 - 72727    

        ticket_nbr, sheet_name = CommitMessageParser(commit_msg).parse_commit_message()

        return ticket_nbr, sheet_name