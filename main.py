import pandas as pd

from s1_technical_analysis.main_processor import make_decisions
from s2_decision_comparison.main_processor import compare_decisions
from email_updater.main_processor import send_updated_decisions
from common_utils.constants.data_paths import DataPaths
from common_utils.constants.others import Others
from common_utils.initial_processors.sleeper import Sleeper

if __name__ == "__main__":

    dp = DataPaths()
    ot = Others()
    sleeper = Sleeper()

    sleeper.initial_sleep(start_hour=12, start_minute=0)
    
    while True:

        updated_decisions = make_decisions()
        previous_decisions = pd.read_csv(dp.latest_decisions_data_path)

        revised_decisions = compare_decisions(updated_decisions, previous_decisions)

        send_updated_decisions(ot.email_address, revised_decisions)

        sleeper.loop_gap_sleep()