from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator


def rsi_crossover_score(price_data, view_length):
    
    rsi_window = 9
    ema_window = 14

    if price_data is None:
        return None
    
    # Calculate RSI
    rsi_indicator = RSIIndicator(close=price_data["close"], window=rsi_window)
    price_data["rsi"] = rsi_indicator.rsi()
    
    # Calculate EMA
    ema_indicator = EMAIndicator(price_data["close"], window=ema_window)
    price_data["ema"] = ema_indicator.ema_indicator()
    
    ### RSI EMA CROSSOVER ###
    crossover_up = (price_data["rsi"] > price_data["ema"]) & (price_data["rsi"].shift(1) <= price_data["ema"].shift(1))
    crossover_down = (price_data["rsi"] < price_data["ema"]) & (price_data["rsi"].shift(1) >= price_data["ema"].shift(1))

    crossover_up_happens = crossover_up.iloc[-1]
    crossover_down_happens = crossover_down.iloc[-1]

    crossover_score = 2 if crossover_up_happens else -2 if crossover_down_happens else 0

    ### RSI TREND ###
    rsi_changes = price_data["rsi"].diff().iloc[-view_length:]
    is_increasing = all(change > 0 for change in rsi_changes)
    is_decreasing = all(change < 0 for change in rsi_changes)

    trend_score = 1 if is_increasing else -1 if is_decreasing else 0

    ### TOTAL SCORE ###
    total_score = crossover_score + trend_score

    # print(f"RSI Crossover Score: {crossover_score}")
    # print(f"RSI Trend Score: {trend_score}")

    return total_score