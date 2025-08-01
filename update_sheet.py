from gspread_dataframe import set_with_dataframe
from import_sheet import import_sheet
from extract_ticket_and_sheet import extract_ticket_and_sheet

def update_sheet(sheet_id, pr_number, status, error_msg, github_token, repo_name, repo_owner):
    ticket_nbr, sheet_name = extract_ticket_and_sheet(pr_number, github_token, repo_name, repo_owner) 
    worksheet, df = import_sheet(sheet_id, sheet_name)

    if ticket_nbr in df['Numéro de ticket'].values:
        df.loc[df['Numéro de ticket'] == ticket_nbr, "Message en cas de problème"] = error_msg
        df.loc[df['Numéro de ticket'] == ticket_nbr, "PR Number"] = "#" + f"{pr_number}"
        if status == "success":
            df.loc[df['Numéro de ticket'] == ticket_nbr, 'Status automatique'] = "Validé"
        elif status == "failure":
            df.loc[df['Numéro de ticket'] == ticket_nbr, 'Status automatique'] = "Erreur de validation"
        else:
            df.loc[df['Numéro de ticket'] == ticket_nbr, 'Status automatique'] = "Aucune information"
    else:
        return f"Numéro de ticket {ticket_nbr} not found in the DataFrame."

    set_with_dataframe(worksheet, df)