import gspread
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials

def import_sheet(sheet_id):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key(sheet_id)

    worksheet = sheet.get_worksheet(0)

    df = get_as_dataframe(worksheet)

    df['Status automatique'] = df['Status automatique'].astype('object')
    df['PR Number'] = df['PR Number'].astype(int)

    return worksheet, df