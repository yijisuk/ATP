from s1_technical_analysis.utils.polygon_api import PolygonAPI

ticker_str = "BTC"
polygonAPI = PolygonAPI(ticker_str, 1)

hourly_price_data = polygonAPI.get_price_data("hour")
daily_price_data = polygonAPI.get_price_data("day")

print(hourly_price_data)
print()
print(daily_price_data)