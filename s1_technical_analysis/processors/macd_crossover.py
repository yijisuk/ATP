from s1_technical_analysis.utils.get_price_data import get_price_data


def macd_crossover_score(ticker_str):

    fast_length = 8
    slow_length = 17
    signal_smoothing = 9

    df = get_price_data(ticker_str)

    if df is None:
        return None

    # Calculate the fast and slow EMAs
    df['fast_ema'] = df['close'].ewm(span=fast_length, adjust=False).mean()
    df['slow_ema'] = df['close'].ewm(span=slow_length, adjust=False).mean()

    # Calculate MACD line (difference between fast EMA and slow EMA)
    df['macd'] = df['fast_ema'] - df['slow_ema']

    # Calculate the Signal line (9-day EMA of the MACD line)
    df['macd_signal'] = df['macd'].ewm(span=signal_smoothing, adjust=False).mean()

    ### MACD CROSSOVER ###
    crossover_up = (df['macd'] > df['macd_signal']) & (df['macd'].shift(1) <= df['macd_signal'].shift(1))
    crossover_down = (df['macd'] < df['macd_signal']) & (df['macd'].shift(1) >= df['macd_signal'].shift(1))

    crossover_up_happens = crossover_up.iloc[-1]
    crossover_down_happens = crossover_down.iloc[-1]

    crossover_score = 2 if crossover_up_happens else -2 if crossover_down_happens else 0

    ### MACD TREND ###
    macd_changes = df['macd'].diff().iloc[-4:]
    is_increasing = all(change > 0 for change in macd_changes)
    is_decreasing = all(change < 0 for change in macd_changes)

    trend_score = 1 if is_increasing else -1 if is_decreasing else 0

    ### TOTAL SCORE ###
    total_score = crossover_score + trend_score

    # print(f"MACD Crossover Score: {crossover_score}")
    # print(f"MACD Trend Score: {trend_score}")

    return total_score