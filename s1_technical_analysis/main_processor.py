from .processors.ichimoku_cloud import ichimoku_score
from .processors.rsi_crossover import rsi_crossover_score
from .processors.macd_crossover import macd_crossover_score


def get_technical_analysis_score(ticker_str):

    # Get the scores
    ichimoku_score_value = ichimoku_score(ticker_str)
    rsi_crossover_score_value = rsi_crossover_score(ticker_str)
    macd_crossover_score_value = macd_crossover_score(ticker_str)

    if ichimoku_score_value is None or rsi_crossover_score_value is None or macd_crossover_score_value is None:
        return None

    # Calculate the total score
    total_score = ichimoku_score_value + rsi_crossover_score_value + macd_crossover_score_value

    if total_score == 0:
        decision = "hold"
    elif total_score < 6:
        decision = "sell"
    elif total_score < 10:
        decision = "buy"
    else:
        decision = "strong-buy"

    return decision