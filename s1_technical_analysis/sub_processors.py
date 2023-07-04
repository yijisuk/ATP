from .processors.ichimoku_cloud import ichimoku_score
from .processors.rsi_crossover import rsi_crossover_score
from .processors.macd_crossover import macd_crossover_score
from .utils.get_price_data import get_price_data

from common_utils.constants.decisions import Decisions


def aggregate_decisions(ticker_str):

    hourly_price_data, daily_price_data = get_price_data(ticker_str)

    hourly_decision = get_technical_analysis_decision(hourly_price_data, view_length=12)
    daily_decision = get_technical_analysis_decision(daily_price_data, view_length=4)

    dc = Decisions()

    ### DAILY EXTREME-BULLISH / BULLISH CASES
    # daily: extreme-bullish THEN extreme-bearish
    if daily_decision == dc.EXTREME_BULLISH:
        final_decision = dc.EXTREME_BULLISH

    # daily: bullish & hourly: >= bullish THEN bullish
    elif daily_decision == dc.BULLISH and \
        (hourly_decision == dc.BULLISH or hourly_decision == dc.EXTREME_BULLISH):
        final_decision = dc.BULLISH

    # daily: bullish & hourly: <= neutral THEN extreme-bearish
    elif daily_decision == dc.BULLISH and \
        (hourly_decision == dc.EXTREME_BEARISH or hourly_decision == dc.BEARISH or hourly_decision == dc.NEUTRAL):
        final_decision = dc.EXTREME_BULLISH

    ### DAILY NEUTRAL CASES
    # daily: neutral & hourly: neutral THEN neutral
    elif daily_decision == dc.NEUTRAL:
        final_decision = dc.NEUTRAL

    ### DAILY EXTREME-BEARISH / BEARISH CASES
    # daily: extreme-bearish & hourly: >= bullish THEN extreme-bullish
    elif daily_decision == dc.EXTREME_BEARISH and \
        (hourly_decision == dc.BULLISH or hourly_decision == dc.EXTREME_BULLISH):
        final_decision = dc.EXTREME_BULLISH

    # daily: extreme-bearish & hourly = neutral THEN bullish
    elif daily_decision == dc.EXTREME_BEARISH and hourly_decision == dc.NEUTRAL:
        final_decision = dc.BULLISH

    # daily: extreme-bearish & hourly: <= bearish THEN extreme-bearish
    elif daily_decision == dc.EXTREME_BEARISH and \
        (hourly_decision == dc.EXTREME_BEARISH or hourly_decision == dc.BEARISH):
        final_decision = dc.EXTREME_BEARISH

    # daily: bearish & hourly >= bullish THEN bullish
    elif daily_decision == dc.BEARISH and \
        (hourly_decision == dc.BULLISH or hourly_decision == dc.EXTREME_BULLISH):
        final_decision = dc.BULLISH

    # daily: bearish & hourly: <= neutral THEN bearish
    elif daily_decision == dc.BEARISH and \
        (hourly_decision == dc.EXTREME_BEARISH or hourly_decision == dc.BEARISH or hourly_decision == dc.NEUTRAL):
        final_decision = dc.BEARISH

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