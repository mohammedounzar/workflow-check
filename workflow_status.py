import requests
import os
from dotenv import load_dotenv

def get_workflow_status(pr_number):
    load_dotenv()

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    REPO_OWNER = os.getenv("REPO_OWNER")
    REPO_NAME = os.getenv("REPO_NAME")

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}"
    pr_data = requests.get(url, headers=headers).json()
    # print(f"Data for PR #{pr_number}: {pr_data}")

    if 'head' not in pr_data:
        return "Erreur PR non trouvée"
    
    sha = pr_data["head"]["sha"]

    # Récupérer les workflows associés à ce commit
    # runs_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs?head_sha={sha}"
    runs_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs?event=pull_request"
    runs_data = requests.get(runs_url, headers=headers).json()

    if "workflow_runs" not in runs_data or not runs_data["workflow_runs"]:
        return "Aucun workflow"

    # Prendre le dernier workflow
    latest_run = runs_data["workflow_runs"][0]
    return latest_run["conclusion"]  # 'success', 'failure', etc.

def main():
    status = get_workflow_status(30)
    print(f"Statut du workflow pour la PR #{30} : {status}")

if __name__ == "__main__":
    main()  