def ichimoku_score(price_data):
    
    window1 = 8
    window2 = 17
    window3 = 55

    if price_data is None:
        return None

    # Calculate Conversion Line (tenkan sen)
    # fl = fast length
    fl_high = price_data['high'].rolling(window=window1).max()
    fl_low = price_data['low'].rolling(window=window1).min()
    price_data['Conversion Line'] = (fl_high + fl_low) / 2

    # Calculate Base Line (kijun sen)
    # sl = slow length
    sl_high = price_data['high'].rolling(window=window2).max()
    sl_low = price_data['low'].rolling(window=window2).min()
    price_data['Base Line'] = (sl_high + sl_low) / 2

    # Calculate Leading Span A (senkou span A)
    price_data['Leading Span A'] = ((price_data['Conversion Line'] + price_data['Base Line']) / 2).shift(window2)

    # Calculate Leading Span B (senkou span B)
    leading_high = price_data['high'].rolling(window=window3).max()
    leading_low = price_data['low'].rolling(window=window3).min()
    price_data['Leading Span B'] = ((leading_high + leading_low) / 2).shift(window2)

    # Calculate Lagging Span (chikou span)
    # df['Lagging Span'] = df['close'].shift(-window2)

    latest_close = price_data["close"].iloc[-1]
    latest_senkou_a = price_data["Leading Span A"].iloc[-1]
    latest_senkou_b = price_data["Leading Span B"].iloc[-1]
    latest_conversion_line = price_data["Conversion Line"].iloc[-1]
    latest_base_line = price_data["Base Line"].iloc[-1]

    ### BASIC TRADING SIGNALS ###
    if (
        latest_close > max(latest_senkou_a, latest_senkou_b) and
        latest_conversion_line > latest_base_line
    ):
        # strong buy
        trading_signal_score = 2
    elif (
        latest_close < min(latest_senkou_a, latest_senkou_b) and
        latest_conversion_line < latest_base_line
    ):
        # strong sell
        trading_signal_score = -2
    elif (
        latest_close > latest_senkou_a or
        latest_conversion_line > latest_base_line
    ):
        # buy
        trading_signal_score = 1
    elif (
        latest_close < latest_senkou_a or
        latest_conversion_line < latest_base_line
    ):
        # sell
        trading_signal_score = -1
    else:
        # neutral
        trading_signal_score = 0

    ### SENKOU A&B CROSSOVERS ###
    senkou_a = price_data["Leading Span A"].iloc[-window2:]
    senkou_b = price_data["Leading Span B"].iloc[-window2:]

    # Detect crossovers
    crossover_up = (senkou_a > senkou_b) & (senkou_a.shift(1) <= senkou_b.shift(1))
    crossover_down = (senkou_a < senkou_b) & (senkou_a.shift(1) >= senkou_b.shift(1))

    crossover_up_happens = crossover_up.any()
    crossover_down_happens = crossover_down.any()

    crossover_score = 2 if crossover_up_happens else -2 if crossover_down_happens else 0

    ### TOTAL SCORE ###
    total_score = trading_signal_score + crossover_score

    # print(f"Ichimoku Trading Signal Score: {trading_signal_score}")
    # print(f"Ichimoku Crossover Score: {crossover_score}")
    
    return total_score