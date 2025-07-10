import re

def rebuild_ticket_nbr(commit_msg):
    """
    Rebuilds the ticket number by removing any leading zeros.
    """
    ticket_nbr = re.findall(r'\b[E]{1,2}[E]?[V]{0,2}2\s*-?\s*\d+\b', commit_msg, re.IGNORECASE)  #  EEV2-1234  , \bEEV2-\d+\b

    print(f"ticket_nbr: {ticket_nbr[0]}")
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

    print(f"ticket_nbr after E and V adjustments: {ticket_nbr}")
    
    count__ = ticket_nbr.count('-')
    if count__ == 0:
        ticket_nbr = ticket_nbr[:4] + "-" + ticket_nbr[4:]
    
    print(f"The result for this input : {commit_msg} is {ticket_nbr}")

    return ticket_nbr

input = "fixed bug in EEV2 5678"
result = rebuild_ticket_nbr("fixed bug in EEV2 5678")  # Example usage
print(f"The result for this input : {input} is {result}")  # Output: EEV2-5678