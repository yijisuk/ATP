from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import ssl
import smtplib
import pandas as pd

from common_utils.constants.data_paths import decisions_data_path
from common_utils.load_agents import get_email_password
from email_updater.utils.format_date import format_date


def send_email(receiver):

    sender = "ioed2023@gmail.com"
    password = get_email_password()

    today = format_date()

    subject = f"{today} Daily Decisions"

    decisions_df = pd.read_csv(decisions_data_path)
    decisions_df['line'] = decisions_df.apply(lambda row: f"{row['tickers']}: {row['decision']}\n", axis=1)
    body_content = "".join(decisions_df['line'])
    
    body = MIMEText(body_content[:-1], "plain")

    em = MIMEMultipart()
    em["From"] = sender
    em["To"] = receiver
    em["Subject"] = subject
    em.attach(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.send_message(em, from_addr = sender, to_addrs = receiver)
        
    except:
        print(f"Got an error while sending the email to {receiver}")