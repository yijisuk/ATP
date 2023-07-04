import pandas as pd

from common_utils.constants.data_paths import DataPaths
from .utils.decision_map import DecisionMap


def compare_decisions(updated_decisions, previous_decisions):

    dp = DataPaths()
    dm = DecisionMap()

    updated_decisions = updated_decisions.set_index("ticker")
    previous_decisions = previous_decisions.set_index("ticker")

    tickers_fin, asset_names_fin, decisions_fin = [], [], []

    for ticker, row in updated_decisions.iterrows():
        try:
            update = updated_decisions.loc[ticker, "decision"]
            prev = previous_decisions.loc[ticker, "decision"]
        except KeyError:
            continue

        if prev is None:
            continue

        revised = dm.decision_map.get((prev, update))
        
        tickers_fin.append(ticker)
        asset_names_fin.append(row["asset_name"])
        decisions_fin.append(revised)

    df = pd.DataFrame({
        "ticker": tickers_fin,
        "asset_name": asset_names_fin,
        "decision": decisions_fin,
    })

    df.to_csv(dp.latest_decisions_data_path, index=False)

    return df