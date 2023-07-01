import pandas as pd

from common_utils.get_tickers import get_tickers
from .sub_processors import get_technical_analysis_score


def make_decisions():

    # print("Getting available tickers...")
    markets = get_tickers()
    krw_market = markets["krw"]
    btc_market = markets["btc"]
    usdt_market = markets["usdt"]

    df = pd.DataFrame({
        "tickers": krw_market.keys(),
        "asset_name": krw_market.values(),
    })

    # print("Getting technical analysis scores...")
    df["decision"] = df.apply(lambda row: get_technical_analysis_score(row["tickers"]), axis=1)
    df.dropna(inplace=True)

    return df