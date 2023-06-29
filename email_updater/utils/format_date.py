from datetime import datetime


def format_date():

    current_date = datetime.now()

    day = current_date.day
    month = current_date.strftime("%B")

    formatted_date = f"{month} {day}{ordinal_suffix(day)}"

    return formatted_date


def ordinal_suffix(day):

    if 4 <= day <= 20 or 24 <= day <= 30:
        return "th"
    
    return ["st", "nd", "rd"][day % 10 - 1]