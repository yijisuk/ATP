from polygon import RESTClient

from common_utils.constants.data_paths import DataPaths


def load_polygon_agent():

    dp = DataPaths()

    with open(dp.polygon_api_key_path, "r") as f:
        client = RESTClient(f.readline())
    
    return client


def load_polygon_api_key():

    dp = DataPaths()

    with open(dp.polygon_api_key_path, "r") as f:
        return f.readline()
    

def get_email_password():

    dp = DataPaths()

    with open(dp.email_password_path, "r") as f:
        password = f.read()
    
    return password