import requests
from datetime import datetime, timezone, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd

from common_utils.load_agents import load_polygon_api_key


class PolygonAPI:

    def __init__(self, ticker_str, years) -> None:

        self.api_key = load_polygon_api_key()
        
        self.ticker_str = ticker_str
        self.years = years


    def get_price_data(self, unit):

        current_date = datetime.now(timezone.utc)
        n_years_ago = (current_date - relativedelta(years=self.years)).replace(minute=0, second=0, microsecond=0)

        if unit == "hour":
            price_df_agg = []
            final_end_time = None

            months_count = 12 * self.years

            for i in range(months_count):

                start_time = n_years_ago + relativedelta(months=i)
                end_time = start_time + relativedelta(months=1)
                final_end_time = end_time
                
                start_time_unix = int(datetime.combine(start_time, datetime.min.time(), tzinfo=timezone.utc).timestamp() * 1000)
                end_time_unix = int(datetime.combine(end_time, datetime.min.time(), tzinfo=timezone.utc).timestamp() * 1000)

                monthly_price_df = self.make_polygon_request(start_time_unix, end_time_unix, unit="hour")
                if monthly_price_df is None:
                    return None

                price_df_agg.append(monthly_price_df)
            
            if current_date - final_end_time > timedelta(hours=1):

                start_time = int(final_end_time.timestamp() * 1000)
                end_time = int(current_date.replace(minute=0, second=0, microsecond=0).timestamp() * 1000)

                remaining_price_df = self.make_polygon_request(start_time, end_time, unit="hour")

                price_df_agg.append(remaining_price_df)

            if len(price_df_agg) == 0:
                return None

            price_df = pd.concat(price_df_agg, ignore_index=True)
            price_df.drop_duplicates(subset='timestamp', inplace=True)
            price_df.reset_index(inplace=True, drop=True)
        
        elif unit == "day":
            start_time_unix = int(n_years_ago.timestamp() * 1000)
            end_time_unix = int(current_date.timestamp() * 1000)

            price_df = self.make_polygon_request(start_time_unix, end_time_unix, unit="day")

        return price_df


    def make_polygon_request(self, start_time, end_time, unit):

        if unit == "hour":
            url = f"https://api.polygon.io/v2/aggs/ticker/X:{self.ticker_str}USD/range/1/hour/{start_time}/{end_time}?adjusted=true&sort=asc&limit=50000&apiKey={self.api_key}"
        elif unit == "day":
            url = f"https://api.polygon.io/v2/aggs/ticker/X:{self.ticker_str}USD/range/1/day/{start_time}/{end_time}?adjusted=true&sort=asc&limit=50000&apiKey={self.api_key}"

        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)

        try:
            price_data = response.json()["results"]
        except KeyError:
            return None

        if len(price_data) == 0:
            return None
        
        price_df = pd.DataFrame(price_data)

        price_df.rename(columns={
            "v": "volume",
            "vw": "volume_weighted",
            "o": "open",
            "c": "close",
            "h": "high",
            "l": "low",
            "t": "timestamp",
            "n": "transactions",
        }, inplace=True)

        return price_df