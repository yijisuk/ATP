from email_updater.processors.email_sender import send_email


def send_updated_decisions(receiver, decisions_df):

    print(f"Sending the daily decisions to {receiver}...")
    send_email(receiver, decisions_df)