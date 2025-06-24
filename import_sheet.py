import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

def import_sheet(sheet_id):
    # Define the scope and credentials
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key(sheet_id)

    worksheet = sheet.get_worksheet(0)

    # Convert it to a pandas DataFrame
    df = get_as_dataframe(worksheet)

    df['Status automatique'] = df['Status automatique'].astype('object')
    df['PR Number'] = df['PR Number'].astype(int)

    return worksheet, df