import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
from import_sheet import import_sheet

def update_sheet(sheet_id, pr_number, status):
    worksheet, df = import_sheet(sheet_id)

    # Update the DataFrame with the new status
    if pr_number in df['PR Number'].values:
        if status == "success":
            df.loc[df['PR Number'] == pr_number, 'Status automatique'] = "Validé"
        elif status == "failure":
            df.loc[df['PR Number'] == pr_number, 'Status automatique'] = "Erreur de validation"
        else:
            df.loc[df['PR Number'] == pr_number, 'Status automatique'] = "Aucune information"
    else:
        print(f"PR Number {pr_number} not found in the DataFrame.")

    set_with_dataframe(worksheet, df)

    print("Sheet updated successfully.")