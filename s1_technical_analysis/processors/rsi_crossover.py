from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator

from s1_technical_analysis.utils.get_price_data import get_price_data


def rsi_crossover_score(ticker_str):
    
    rsi_window = 9
    ema_window = 14
    
    # Fetch the price data
    df = get_price_data(ticker_str)

    if df is None:
        return None
    
    # Calculate RSI
    rsi_indicator = RSIIndicator(close=df["close"], window=rsi_window)
    df["rsi"] = rsi_indicator.rsi()
    
    # Calculate EMA
    ema_indicator = EMAIndicator(df["close"], window=ema_window)
    df["ema"] = ema_indicator.ema_indicator()
    
    ### RSI EMA CROSSOVER ###
    crossover_up = (df["rsi"] > df["ema"]) & (df["rsi"].shift(1) <= df["ema"].shift(1))
    crossover_down = (df["rsi"] < df["ema"]) & (df["rsi"].shift(1) >= df["ema"].shift(1))

    crossover_up_happens = crossover_up.iloc[-1]
    crossover_down_happens = crossover_down.iloc[-1]

    crossover_score = 2 if crossover_up_happens else -2 if crossover_down_happens else 0

    ### RSI TREND ###
    rsi_changes = df["rsi"].diff().iloc[-4:]
    is_increasing = all(change > 0 for change in rsi_changes)
    is_decreasing = all(change < 0 for change in rsi_changes)

    trend_score = 1 if is_increasing else -1 if is_decreasing else 0

    ### TOTAL SCORE ###
    total_score = crossover_score + trend_score

    # print(f"RSI Crossover Score: {crossover_score}")
    # print(f"RSI Trend Score: {trend_score}")

    return total_score