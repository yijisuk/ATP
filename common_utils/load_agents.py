from polygon import RESTClient

from common_utils.constants.data_paths import polygon_api_key_path, email_password_path


def load_polygon_agent():

    with open(polygon_api_key_path, "r") as f:
        client = RESTClient(f.readline())
    
    return client


def load_polygon_api_key():

    with open(polygon_api_key_path, "r") as f:
        return f.readline()
    

def get_email_password():

    with open(email_password_path, "r") as f:
        password = f.read()
    
    return password