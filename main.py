from s1_technical_analysis.main_processor import make_daily_decisions
from email_updater.main_processor import send_daily_decisions
from common_utils.file_date_check import is_file_created_within_12_hours
from common_utils.constants.data_paths import decisions_data_path

if __name__ == "__main__":

    if not is_file_created_within_12_hours(decisions_data_path):
        make_daily_decisions()

    email = "offconstruction@gmail.com"
    send_daily_decisions(email)

    print("Done!")