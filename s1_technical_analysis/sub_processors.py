from .processors.ichimoku_cloud import ichimoku_score
from .processors.rsi_crossover import rsi_crossover_score
from .processors.macd_crossover import macd_crossover_score
from .utils.get_price_data import get_price_data

from common_utils.constants.decisions import Decisions
from .utils.decision_map import DecisionMap


def aggregate_decisions(ticker_str):

    hourly_price_data, daily_price_data = get_price_data(ticker_str)

    hourly_decision = get_technical_analysis_decision(hourly_price_data, view_length=12)
    daily_decision = get_technical_analysis_decision(daily_price_data, view_length=4)

    dc = Decisions()
    dm = DecisionMap()

    daily_map = dm.decision_map.get(daily_decision, dc.NEUTRAL)

    # If the daily_map is a dictionary, then we look up based on the hourly_decision
    # Otherwise, we use the daily_map as the final decision
    final_decision = daily_map.get(hourly_decision, daily_map) if isinstance(daily_map, dict) else daily_map

    return final_decision


def get_technical_analysis_decision(price_data, view_length):

    # Get the hourly evaluation scores
    ichimoku_score_value = ichimoku_score(price_data)
    rsi_crossover_score_value = rsi_crossover_score(price_data, view_length)
    macd_crossover_score_value = macd_crossover_score(price_data, view_length)

    if ichimoku_score_value is None or rsi_crossover_score_value is None or macd_crossover_score_value is None:
        return None

    # Calculate the total score
    total_score = ichimoku_score_value + rsi_crossover_score_value + macd_crossover_score_value

    if total_score == -10:
        decision = "extreme-bearish"
    elif total_score < 0:
        decision = "bearish"
    elif total_score == 0:
        decision = "neutral"
    elif 5 <= total_score < 10:
        decision = "bullish"
    else:
        decision = "extreme-bullish"

    return decision