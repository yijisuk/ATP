from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
import pandas as pd
from pybit.unified_trading import HTTP


class BybitAPI:

    def __init__(self, ticker_str, category, years) -> None:
        
        self.ticker_str = ticker_str
        self.category = category    # available categories: spot, linear, inverse
        self.years = years

        self.session = HTTP(testnet=True)

        current_time = datetime.now(timezone.utc)
        n_years_ago = (current_time - relativedelta(years=years)).replace(minute=0, second=0, microsecond=0)

        self.current_time_unix = current_time.timestamp() * 1000
        self.n_years_ago_unix = datetime.combine(n_years_ago, datetime.min.time(), tzinfo=timezone.utc).timestamp() * 1000


    def get_price_data(self, unit):

        if unit == "hour":
            interval = 60
            single_loop_data_count = 8

        elif unit == "day":
            interval = "D"
            single_loop_data_count = 200

        diff = self.current_time_unix - self.n_years_ago_unix
        single_hour_unix = 60 * 60 * 1000
        single_day_unix = 24 * single_hour_unix

        single_loop_unix = single_loop_data_count * single_day_unix
        loop_count = int(diff / single_loop_unix)

        aggregated_data = []

        # Main loop
        for i in range(loop_count):
            try:
                start_unix = int(self.n_years_ago_unix + (single_loop_unix * i))
                end_unix = int(start_unix + single_loop_unix - single_hour_unix)

                response = self.session.get_kline(
                    category=self.category,
                    symbol=f"{self.ticker_str}USDT",
                    interval=interval,
                    start=start_unix,
                    end=end_unix,
                )

                price_data = response["result"]["list"][::-1]
                aggregated_data.extend(price_data)

            except:
                return None

        if len(aggregated_data) == 0:
            return None

        # Remaining data
        remaining_unix = diff % single_loop_unix
        if remaining_unix > 0:
            start_unix = int(self.n_years_ago_unix + (single_loop_unix * loop_count))
            end_unix = int(self.current_time_unix)

            try:
                response = self.session.get_kline(
                    category=self.category,
                    symbol=f"{self.ticker_str}USDT",
                    interval=interval,
                    start=start_unix,
                    end=end_unix,
                )

                price_data = response["result"]["list"][::-1]
                aggregated_data.extend(price_data)

            except:
                return None

        # Merge into a single dataframe
        price_agg = []
        for unit_price_data in aggregated_data:

            timestamp = int(unit_price_data[0])
            open_price = float(unit_price_data[1])
            high_price = float(unit_price_data[2])
            low_price = float(unit_price_data[3])
            close_price = float(unit_price_data[4])
            volume = float(unit_price_data[5])

            hourly_price_df = pd.DataFrame([{
                "open": open_price,
                "high": high_price,
                "low": low_price,
                "close": close_price,
                "volume": volume,
                "timestamp": timestamp,
            }])

            price_agg.append(hourly_price_df)

        price_df = pd.concat(price_agg, ignore_index=True)
        price_df.reset_index(drop=True, inplace=True)

        return price_df