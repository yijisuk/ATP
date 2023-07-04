from common_utils.constants.decisions import Decisions


class DecisionMap():

    dc = Decisions()

    decision_map = {
        dc.EXTREME_BULLISH: dc.EXTREME_BULLISH,
        dc.BULLISH: {
            dc.BULLISH: dc.BULLISH,
            dc.EXTREME_BULLISH: dc.BULLISH,
            dc.EXTREME_BEARISH: dc.EXTREME_BULLISH,
            dc.BEARISH: dc.EXTREME_BULLISH,
            dc.NEUTRAL: dc.EXTREME_BULLISH,
        },
        dc.NEUTRAL: dc.NEUTRAL,
        dc.EXTREME_BEARISH: {
            dc.BULLISH: dc.EXTREME_BULLISH,
            dc.EXTREME_BULLISH: dc.EXTREME_BULLISH,
            dc.NEUTRAL: dc.BULLISH,
            dc.EXTREME_BEARISH: dc.EXTREME_BEARISH,
            dc.BEARISH: dc.EXTREME_BEARISH,
        },
        dc.BEARISH: {
            dc.BULLISH: dc.BULLISH,
            dc.EXTREME_BULLISH: dc.BULLISH,
            dc.EXTREME_BEARISH: dc.BEARISH,
            dc.BEARISH: dc.BEARISH,
            dc.NEUTRAL: dc.BEARISH,
        },
    }