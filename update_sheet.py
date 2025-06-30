from gspread_dataframe import set_with_dataframe
from import_sheet import import_sheet

def update_sheet(sheet_id, pr_number, status, error_msg):
    worksheet, df = import_sheet(sheet_id)

    # Update the DataFrame with the new status
    if pr_number in df['PR Number'].values:
        df.loc[df['PR Number'] == pr_number, "Message en cas de problème"] = error_msg
        if status == "success":
            df.loc[df['PR Number'] == pr_number, 'Status automatique'] = "Validé"
        elif status == "failure":
            df.loc[df['PR Number'] == pr_number, 'Status automatique'] = "Erreur de validation"
        else:
            df.loc[df['PR Number'] == pr_number, 'Status automatique'] = "Aucune information"
    else:
        return f"PR Number {pr_number} not found in the DataFrame."

    set_with_dataframe(worksheet, df)

    print("Sheet updated successfully.")