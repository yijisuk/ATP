import pandas as pd

from common_utils.get_tickers import get_tickers
from .sub_processors import aggregate_decisions
from common_utils.constants.data_paths import DataPaths


def make_decisions():

    # print("Getting available tickers...")
    markets = get_tickers()
    krw_market = markets["krw"]
    # btc_market = markets["btc"]
    # usdt_market = markets["usdt"]

    df = pd.DataFrame({
        "ticker": krw_market.keys(),
        "asset_name": krw_market.values(),
    })

    # print("Getting technical analysis scores...")
    df["decision"] = df.apply(lambda row: aggregate_decisions(row["ticker"]), axis=1)
    df.dropna(inplace=True)

    dp = DataPaths()
    df.to_csv(dp.latest_decisions_data_path, index=False)

    return df