import os

class DataPaths():

    root_path = "/home/yijisuk/si.ver-I"
    # root_path = os.path.join("home", "yijisuk", "si.ver-I")

    # polygon_api_key_path = root_path + "/api_keys/polygon_api_key.txt"
    polygon_api_key_path = os.path.join("api_keys", "polygon_api_key.txt")

    # email_password_path = root_path + "/api_keys/email_password.txt"
    email_password_path = os.path.join("api_keys", "email_password.txt")

    # latest_decisions_data_path = root_path + "/data_storage/daily_decisions.csv"
    latest_decisions_data_path = os.path.join("data_storage", "latest_decisions.csv")