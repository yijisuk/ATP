import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
from pycoingecko import CoinGeckoAPI

from common_utils.load_agents import load_polygon_api_key


def get_price_data(ticker_str, ticker_name):

    price_data = polygon_api(ticker_str)

    if price_data is None:
        price_data = coingecko_api(ticker_name)
    
    return price_data


def polygon_api(ticker_str):

    current_date = datetime.now()
    one_year_ago = current_date - relativedelta(years=1)

    current_date_str = current_date.strftime("%Y-%m-%d")
    one_year_ago_str = one_year_ago.strftime("%Y-%m-%d")

    api_key = load_polygon_api_key()

    url = f"https://api.polygon.io/v2/aggs/ticker/X:{ticker_str}USD/range/1/day/{one_year_ago_str}/{current_date_str}?adjusted=true&sort=asc&limit=50000&apiKey={api_key}"
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


def coingecko_api(ticker_name):

    cg = CoinGeckoAPI()

    try:
        price_data = cg.get_coin_ohlc_by_id(id=ticker_name, vs_currency="usd", days="365", precision="18")
    except:
        return None

    columns = ["open", "high", "close", "low"]
    price_list = [dict(zip(columns, daily_price[1:])) for daily_price in price_data]

    price_df = pd.DataFrame(price_list)

    return price_df