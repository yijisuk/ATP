def macd_crossover_score(price_data):

    fast_length = 8
    slow_length = 17
    signal_smoothing = 9

    if price_data is None:
        return None

    # Calculate the fast and slow EMAs
    price_data['fast_ema'] = price_data['close'].ewm(span=fast_length, adjust=False).mean()
    price_data['slow_ema'] = price_data['close'].ewm(span=slow_length, adjust=False).mean()

    # Calculate MACD line (difference between fast EMA and slow EMA)
    price_data['macd'] = price_data['fast_ema'] - price_data['slow_ema']

    # Calculate the Signal line (9-day EMA of the MACD line)
    price_data['macd_signal'] = price_data['macd'].ewm(span=signal_smoothing, adjust=False).mean()

    ### MACD CROSSOVER ###
    crossover_up = (price_data['macd'] > price_data['macd_signal']) & (price_data['macd'].shift(1) <= price_data['macd_signal'].shift(1))
    crossover_down = (price_data['macd'] < price_data['macd_signal']) & (price_data['macd'].shift(1) >= price_data['macd_signal'].shift(1))

    crossover_up_happens = crossover_up.iloc[-1]
    crossover_down_happens = crossover_down.iloc[-1]

    crossover_score = 2 if crossover_up_happens else -2 if crossover_down_happens else 0

    ### MACD TREND ###
    view_length = 12
    macd_changes = price_data['macd'].diff().iloc[-view_length:]
    is_increasing = all(change > 0 for change in macd_changes)
    is_decreasing = all(change < 0 for change in macd_changes)

    trend_score = 1 if is_increasing else -1 if is_decreasing else 0

    ### TOTAL SCORE ###
    total_score = crossover_score + trend_score

    # print(f"MACD Crossover Score: {crossover_score}")
    # print(f"MACD Trend Score: {trend_score}")

    return total_score