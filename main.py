from import_sheet import import_sheet
from update_sheet import update_sheet
from workflow_status import get_workflow_status
from dotenv import load_dotenv
import os
import time

def main():
    sheet_id = os.getenv("SHEET_ID")
    status = os.getenv("VALIDATION_STATUS")
    pr_number = os.getenv("PR_NUMBER") 

    update_sheet(sheet_id, pr_number, status)

if __name__ == "__main__":
    load_dotenv() 
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}")