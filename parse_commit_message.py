import re

class CommitMessageParser:
    def __init__(self, commit_msg):
        self.commit_msg = commit_msg
    
    def parse_commit_message(self):
        ticket_nbr = re.findall(r'\b[E]{1,2}\s*[E]?\s*[V]{0,2}\s*2\s*-?\s*\d+\b', self.commit_msg, re.IGNORECASE)  #  EEV2-1234  , \bEEV2-\d+\b

        # rebuild ticket numbers

        ticket_nbr = ticket_nbr[0].upper().replace(' ', '')

        count_e = ticket_nbr.count('E')
        if count_e == 1:
            ticket_nbr = "E" + ticket_nbr
        
        elif count_e == 3:
            ticket_nbr = ticket_nbr[1:]
        
        count_v = ticket_nbr.count('V')
        if count_v == 0:
            ticket_nbr = ticket_nbr[:2] + 'V' + ticket_nbr[2:]

        elif count_v == 2:
            ticket_nbr = ticket_nbr[:3] + ticket_nbr[4:]
        
        count__ = ticket_nbr.count('-')
        if count__ == 0:
            ticket_nbr = ticket_nbr[:4] + "-" + ticket_nbr[4:]
        
        if ticket_nbr:
            print(f"Ticket number found: {ticket_nbr}")
        else:
            raise ValueError("No valid ticket number found in commit message.")
        
        sheet_name = re.findall(r'\b[r]?[R]?elease\s*-?\s*\d+\.\d+\.\d+\b', self.commit_msg)  # release-1.2.3   

        sheet_name = sheet_name[0].lower().replace(' ', '')

        count__sn = sheet_name.count("-")    
        if count__sn == 0:   # release1.2.3 
            print(f"Release number found: {sheet_name[7:]}")
            sheet_name = "release" + "-" + sheet_name[7:]

        if sheet_name:  
            print(f"Sheet name found: {sheet_name}")
        else:
            raise ValueError("No valid sheet name found in commit message.")
        
        return ticket_nbr, sheet_name

print(f"test: {CommitMessageParser('Release-1.2.3 EEv2 1234').parse_commit_message()}")  # test: ('EEV2-1234', 'release-1.2.3')