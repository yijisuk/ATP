import time
from datetime import datetime, timedelta

from s1_technical_analysis.main_processor import make_decisions
from email_updater.main_processor import send_hourly_decisions

if __name__ == "__main__":

    start_hour = 20
    start_minute = 0

    current_time = datetime.now()

    next_start = current_time.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
    if next_start <= current_time:
        next_start += timedelta(days=1)

    initial_sleep_seconds = (next_start - current_time).total_seconds()
    time.sleep(initial_sleep_seconds)
    
    while True:
        # TODO: screen the market data on a hourly basis, if a buy signal is detected, send an email to the user
        # a buy signal is only generated when both the daily and hourly basis signals are "buy"

        # TODO: market data evaluation on a daily basis

        hourly_decisions = make_decisions()

        email = "offconstruction@gmail.com"
        send_hourly_decisions(email, hourly_decisions)

        # print("Done!")
        print(f"Results for {datetime.now().strftime('%H')}:00 have been sent.")

        next_hour = (current_time.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1))
        sleep_seconds = (next_hour - current_time).total_seconds()

        time.sleep(sleep_seconds)