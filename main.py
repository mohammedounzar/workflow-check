from import_sheet import import_sheet
from update_sheet import update_sheet
from workflow_status import get_workflow_status
from dotenv import load_dotenv
import os
import time

def main():
    sheet_id = os.getenv("SHEET_ID")

    df = import_sheet(sheet_id)[1]  
    
    # Créer un dictionnaire pour stocker les statuts des PRs
    pr_status_map = {}

    for pr_number in df['PR Number'].unique():
        status = get_workflow_status(pr_number)
        print(f"Statut du workflow pour la PR #{pr_number} : {status}")
        pr_status_map[pr_number] = status

    update_sheet(sheet_id, pr_status_map)

if __name__ == "__main__":
    load_dotenv() 
    while True:
        try:
            main()
        except Exception as e:
            print(f"Error occurred: {e}")
        time.sleep(30)