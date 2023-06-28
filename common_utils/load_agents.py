from polygon import RESTClient


def load_polygon_agent():

    with open("./api_keys/polygon_api_key.txt", "r") as f:
        client = RESTClient(f.readline())
    
    return client


def load_polygon_api_key():
    
    with open("./api_keys/polygon_api_key.txt", "r") as f:
        return f.readline()