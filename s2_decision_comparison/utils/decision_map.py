from common_utils.constants.decisions import Decisions


class DecisionMap():

    dc = Decisions()

    decision_map = {
        (dc.EXTREME_BULLISH, dc.EXTREME_BULLISH): dc.EXTREME_BEARISH,
        (dc.EXTREME_BULLISH, dc.BULLISH): dc.BEARISH,
        (dc.EXTREME_BULLISH, dc.NEUTRAL): dc.BEARISH,
        (dc.EXTREME_BULLISH, dc.BEARISH): dc.NEUTRAL,
        (dc.EXTREME_BULLISH, dc.EXTREME_BEARISH): dc.NEUTRAL,

        (dc.BULLISH, dc.EXTREME_BULLISH): dc.BEARISH,
        (dc.BULLISH, dc.BULLISH): dc.NEUTRAL,
        (dc.BULLISH, dc.NEUTRAL): dc.NEUTRAL,
        (dc.BULLISH, dc.BEARISH): dc.BULLISH,
        (dc.BULLISH, dc.EXTREME_BEARISH): dc.EXTREME_BULLISH,

        (dc.NEUTRAL, dc.EXTREME_BULLISH): dc.BULLISH,
        (dc.NEUTRAL, dc.BULLISH): dc.NEUTRAL,
        (dc.NEUTRAL, dc.NEUTRAL): dc.NEUTRAL,
        (dc.NEUTRAL, dc.BEARISH): dc.NEUTRAL,
        (dc.NEUTRAL, dc.EXTREME_BEARISH): dc.BEARISH,

        (dc.BEARISH, dc.EXTREME_BULLISH): dc.EXTREME_BULLISH,
        (dc.BEARISH, dc.BULLISH): dc.BULLISH,
        (dc.BEARISH, dc.NEUTRAL): dc.NEUTRAL,
        (dc.BEARISH, dc.BEARISH): dc.NEUTRAL,
        (dc.BEARISH, dc.EXTREME_BEARISH): dc.BEARISH,

        (dc.EXTREME_BEARISH, dc.EXTREME_BULLISH): dc.NEUTRAL,
        (dc.EXTREME_BEARISH, dc.BULLISH): dc.NEUTRAL,
        (dc.EXTREME_BEARISH, dc.NEUTRAL): dc.BEARISH,
        (dc.EXTREME_BEARISH, dc.BEARISH): dc.EXTREME_BEARISH,
        (dc.EXTREME_BEARISH, dc.EXTREME_BEARISH): dc.EXTREME_BEARISH
    }


class OldDecisionMap():

    dc = Decisions()

    decision_map = {
        (dc.EXTREME_BULLISH, dc.EXTREME_BULLISH): dc.EXTREME_BULLISH,
        (dc.EXTREME_BULLISH, dc.BULLISH): dc.BULLISH,
        (dc.EXTREME_BULLISH, dc.NEUTRAL): dc.BEARISH,
        (dc.EXTREME_BULLISH, dc.BEARISH): dc.EXTREME_BEARISH,
        (dc.EXTREME_BULLISH, dc.EXTREME_BEARISH): dc.EXTREME_BEARISH,

        (dc.BULLISH, dc.EXTREME_BULLISH): dc.EXTREME_BULLISH,
        (dc.BULLISH, dc.BULLISH): dc.BULLISH,
        (dc.BULLISH, dc.NEUTRAL): dc.BEARISH,
        (dc.BULLISH, dc.BEARISH): dc.EXTREME_BEARISH,
        (dc.BULLISH, dc.EXTREME_BEARISH): dc.EXTREME_BEARISH, # This case seems wrong in original code, just copied it here

        (dc.NEUTRAL, dc.EXTREME_BULLISH): dc.EXTREME_BULLISH,
        (dc.NEUTRAL, dc.BULLISH): dc.BULLISH,
        (dc.NEUTRAL, dc.NEUTRAL): dc.NEUTRAL,
        (dc.NEUTRAL, dc.BEARISH): dc.BEARISH,
        (dc.NEUTRAL, dc.EXTREME_BEARISH): dc.EXTREME_BEARISH,

        (dc.BEARISH, dc.EXTREME_BULLISH): dc.EXTREME_BULLISH,
        (dc.BEARISH, dc.BULLISH): dc.EXTREME_BULLISH,
        (dc.BEARISH, dc.NEUTRAL): dc.BULLISH,
        (dc.BEARISH, dc.BEARISH): dc.BEARISH,
        (dc.BEARISH, dc.EXTREME_BEARISH): dc.EXTREME_BEARISH,

        (dc.EXTREME_BEARISH, dc.EXTREME_BULLISH): dc.EXTREME_BULLISH,
        (dc.EXTREME_BEARISH, dc.BULLISH): dc.EXTREME_BULLISH,
        (dc.EXTREME_BEARISH, dc.NEUTRAL): dc.BULLISH,
        (dc.EXTREME_BEARISH, dc.BEARISH): dc.BEARISH,
        (dc.EXTREME_BEARISH, dc.EXTREME_BEARISH): dc.EXTREME_BEARISH
    }