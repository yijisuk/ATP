import time
from datetime import datetime, timedelta


class Sleeper():

    def __init__(self) -> None:
        
        self.current_time = datetime.now()


    def initial_sleep(self, start_hour, start_minute):

        next_start = self.current_time.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
        if next_start <= self.current_time:
            next_start += timedelta(days=1)

        initial_sleep_seconds = (next_start - self.current_time).total_seconds()
        time.sleep(initial_sleep_seconds)


    def loop_gap_sleep(self):

        self.current_time = datetime.now()
        next_hour = (self.current_time.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1))
        sleep_seconds = (next_hour - self.current_time).total_seconds()

        time.sleep(sleep_seconds)