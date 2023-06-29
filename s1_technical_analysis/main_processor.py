import pandas as pd

from common_utils.get_tickers import get_tickers
from common_utils.constants.data_paths import decisions_data_path
from .sub_processors import get_technical_analysis_score


def daily_decisions():

    print("Getting available tickers...")
    markets = get_tickers()
    krw_market = markets["krw"]
    btc_market = markets["btc"]
    usdt_market = markets["usdt"]

    df = pd.DataFrame({
        "tickers": krw_market.keys(),
        "asset_name": krw_market.values(),
    })

    print("Getting technical analysis scores...")
    df["decision"] = df.apply(lambda row: get_technical_analysis_score(row["tickers"], row["asset_name"]), axis=1)
    df.dropna(inplace=True)
    
    print("Saving the decisions data...")
    df.to_csv(decisions_data_path, index=False)

    print("Done!")