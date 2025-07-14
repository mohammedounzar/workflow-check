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

    print(f"Commit msg: {commit_msg}")    #  EE2 - 72727    

    ticket_nbr = re.findall(r'\b[E]{1,2}[E]?[V]{0,2}2\s*-?\s*\d+\b', commit_msg, re.IGNORECASE)  #  EEV2-1234  , \bEEV2-\d+\b

    # rebuild ticket numbers

    ticket_nbr = ticket_nbr[0].upper().replace(' ', '')

    count_e = ticket_nbr.count('E')
    if count_e == 1:
        ticket_nbr = "E" + ticket_nbr
    
    elif count_e == 3:
        ticket_nbr = ticket_nbr[1:]
    
    count_v = ticket_nbr.count('V')
    if count_v == 0:
        ticket_nbr = ticket_nbr[:2] + 'V' + ticket_nbr[2:]

    elif count_v == 2:
        ticket_nbr = ticket_nbr[:3] + ticket_nbr[4:]
    
    count__ = ticket_nbr.count('-')
    if count__ == 0:
        ticket_nbr = ticket_nbr[:4] + "-" + ticket_nbr[4:]
    
    if ticket_nbr:
        print(f"Ticket number found: {ticket_nbr}")
    else:
        raise ValueError("No valid ticket number found in commit message.")
    
    sheet_name = re.findall(r'\brelease\s*-?\s*\d+\.\d+\.\d+\b', commit_msg)  # release-1.2.3   

    sheet_name = sheet_name[0].lower().replace(' ', '')

    sheet_name = sheet_name[0]

    count__sn = sheet_name.count("-")    
    if count__sn == 0:   # release1.2.3 
        sheet_name = "release" + "-" + sheet_name[7:]

    if sheet_name:  
        print(f"Sheet name found: {sheet_name[0]}")
    else:
        raise ValueError("No valid sheet name found in commit message.")
    
    return ticket_nbr, sheet_name[0]