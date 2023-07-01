import os
import datetime


def is_file_created_within_12_hours(file_path):

    # Get the current time
    current_time = datetime.datetime.now()

    # Get the creation time of the file
    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

    # Calculate the time difference between the current time and creation time
    time_difference = current_time - creation_time

    # Check if the time difference is less than or equal to 12 hours
    return time_difference.total_seconds() <= 12 * 3600