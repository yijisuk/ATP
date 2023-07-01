from .polygon_api import PolygonAPI
from .bybit_api import BybitAPI


def get_price_data(ticker_str):

    polygonAPI = PolygonAPI(ticker_str, 1)

    hourly_price_data = polygonAPI.get_price_data("hour")
    daily_price_data = polygonAPI.get_price_data("day")

    if hourly_price_data is None or daily_price_data is None:
        
        bybitAPI = BybitAPI(ticker_str, "spot", 1)

        hourly_price_data = bybitAPI.get_price_data("hour")
        daily_price_data = bybitAPI.get_price_data("day")

    return (hourly_price_data, daily_price_data)