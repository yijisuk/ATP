from email_updater.processors.email_sender import send_email


def send_daily_decisions(receiver):

    print(f"Sending the daily decisions to {receiver}...")
    send_email(receiver)