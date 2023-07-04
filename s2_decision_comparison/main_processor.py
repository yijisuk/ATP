import pandas as pd

from common_utils.constants.decisions import Decisions
from common_utils.constants.data_paths import DataPaths


def compare_decisions(updated_decisions, previous_decisions):

    dc = Decisions()
    dp = DataPaths()

    tickers = list(updated_decisions["ticker"])
    asset_names = list(updated_decisions["asset_name"])

    tickers_fin, asset_names_fin, decisions_fin = [], [], []

    for ticker, asset_name in zip(tickers, asset_names):
        update = updated_decisions[updated_decisions["ticker"] == ticker]["decision"].iloc[0]
        prev = previous_decisions[previous_decisions["ticker"] == ticker]["decision"].iloc[0]

        if prev is None:
            continue

        ### ----- ORIG EXTREME-BULLISH
        # extreme-bullish -> extreme-bullish THEN extreme-bullish
        if prev == dc.EXTREME_BULLISH and update == dc.EXTREME_BULLISH:
            revised = dc.EXTREME_BULLISH

        # extreme-bullish -> bullish THEN bullish
        elif prev == dc.EXTREME_BULLISH and update == dc.BULLISH:
            revised = dc.BULLISH

        # extreme-bullish -> neutral THEN bearish
        elif prev == dc.EXTREME_BULLISH and update == dc.NEUTRAL:
            revised = dc.BEARISH

        # extreme-bullish -> bearish THEN extreme-bearish
        elif prev == dc.EXTREME_BULLISH and update == dc.BEARISH:
            revised = dc.EXTREME_BEARISH

        # extreme-bullish -> extreme-bearish THEN extreme-bearish
        elif prev == dc.EXTREME_BULLISH and update == dc.EXTREME_BEARISH:
            revised = dc.EXTREME_BEARISH

        ### ----- ORIG BULLISH
        # bullish -> extreme-bullish THEN extreme-bullish
        elif prev == dc.BULLISH and update == dc.EXTREME_BULLISH:
            revised = dc.EXTREME_BULLISH

        # bullish -> bullish THEN bullish
        elif prev == dc.BULLISH and update == dc.BULLISH:
            revised = dc.BULLISH

        # bullish -> neutral THEN bearish
        elif prev == dc.BULLISH and update == dc.NEUTRAL:
            revised = dc.BEARISH

        # bullish -> bearish THEN extreme-bearish
        elif prev == dc.BULLISH and update == dc.BEARISH:
            revised = dc.EXTREME_BEARISH

        # bullish -> extreme-bullish THEN extreme-bearish
        elif prev == dc.BULLISH and update == dc.EXTREME_BULLISH:
            revised = dc.EXTREME_BEARISH

        ### ----- ORIG NEUTRAL
        # neutral -> extreme-bullish THEN extreme-bullish
        elif prev == dc.NEUTRAL and update == dc.EXTREME_BULLISH:
            revised = dc.EXTREME_BULLISH

        # neutral -> bullish THEN bullish
        elif prev == dc.NEUTRAL and update == dc.BULLISH:
            revised = dc.BULLISH

        # neutral -> neutral THEN neutral
        elif prev == dc.NEUTRAL and update == dc.NEUTRAL:
            revised = dc.NEUTRAL

        # neutral -> bearish THEN bearish
        elif prev == dc.NEUTRAL and update == dc.BEARISH:
            revised = dc.BEARISH

        # neutral -> extreme-bearish THEN extreme-bearish
        elif prev == dc.NEUTRAL and update == dc.EXTREME_BEARISH:
            revised = dc.EXTREME_BEARISH

        ### ----- ORIG BEARISH
        # bearish -> extreme-bullish THEN extreme-bullish
        elif prev == dc.BEARISH and update == dc.EXTREME_BULLISH:
            revised = dc.EXTREME_BULLISH

        # bearish -> bullish THEN extreme-bullish
        elif prev == dc.BEARISH and update == dc.BULLISH:
            revised = dc.EXTREME_BULLISH

        # bearish -> neutral THEN bullish
        elif prev == dc.BEARISH and update == dc.NEUTRAL:
            revised = dc.BULLISH

        # bearish -> bearish THEN bearish
        elif prev == dc.BEARISH and update == dc.BEARISH:
            revised = dc.BEARISH

        # bearish -> extreme-bearish THEN extreme-bearish
        elif prev == dc.BEARISH and update == dc.EXTREME_BEARISH:
            revised = dc.EXTREME_BEARISH

        ### ----- ORIG EXTREME-BEARISH
        # extreme-bearish -> extreme-bullish THEN extreme-bullish
        elif prev == dc.EXTREME_BEARISH and update == dc.EXTREME_BULLISH:
            revised = dc.EXTREME_BULLISH

        # extreme-bearish -> bullish THEN extreme-bullish
        elif prev == dc.EXTREME_BEARISH and update == dc.BULLISH:
            revised = dc.EXTREME_BULLISH

        # extreme-bearish -> neutral THEN bullish
        elif prev == dc.EXTREME_BEARISH and update == dc.NEUTRAL:
            revised = dc.BULLISH

        # extreme-bearish -> bearish THEN bearish
        elif prev == dc.EXTREME_BEARISH and update == dc.BEARISH:
            revised = dc.BEARISH

        # extreme-bearish -> extreme-bearish THEN extreme-bearish
        elif prev == dc.EXTREME_BEARISH and update == dc.EXTREME_BEARISH:
            revised = dc.EXTREME_BEARISH

        tickers_fin.apped(ticker)
        asset_names_fin.append(asset_name)
        decisions_fin.append(revised)

    df = pd.DataFrame({
        "ticker": tickers_fin,
        "asset_name": asset_names_fin,
        "decision": decisions_fin,
    })

    df.to_csv(dp.latest_decisions_data_path, index=False)

    return df