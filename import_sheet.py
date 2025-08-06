import gspread
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials

def import_sheet(sheet_id, sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key(sheet_id)
    worksheets = sheet.worksheets()  
    
    norm_pattern = sheet_name.lower().replace('-', '').replace(' ', '')  # release-7.0.1
    
    for ws in worksheets:
        norm_title = ws.title.lower().replace('-', '').replace(' ', '')  # 24-06-2025-ebsrelease7.0.1
        if norm_pattern in norm_title:
            df = get_as_dataframe(ws)
            df['Status automatique'] = df['Status automatique'].astype('object')
            df['Message en cas de problème'] = df['Message en cas de problème'].astype('object')
            return ws, df
    
    raise ValueError(f"No worksheet found matching pattern '{sheet_name}'")