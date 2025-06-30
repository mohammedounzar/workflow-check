from update_sheet import update_sheet
import os

def main():
    sheet_id = os.getenv("SHEET_ID")
    status = os.getenv("VALIDATION_STATUS")
    error_msg = os.getenv("ERROR_MSG")
    pr_number = int(os.getenv("PR_NUMBER"))
    print(f"Sheet ID: {sheet_id}, Status: {status}, PR Number: {pr_number}")

    if not all([sheet_id, status, pr_number]):
        raise ValueError("Missing one or more required environment variables.")

    update_sheet(sheet_id, pr_number, status, error_msg)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}")