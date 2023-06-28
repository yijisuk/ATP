import requests


def get_tickers():

    url = "https://api.upbit.com/v1/market/all?isDetails=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    ticker_agg = response.json()
    krw_market, btc_market, usdt_market = [], [], []

    for ticker_details in ticker_agg:

        market, ticker = ticker_details["market"].split("-")

        if "KRW" in market:
            krw_market.append(ticker)
        
        elif "BTC" in market:
            btc_market.append(ticker)
        
        elif "USDT" in market:
            usdt_market.append(ticker)
    
    markets = {"krw": krw_market, "btc": btc_market, "usdt": usdt_market}
    
    return markets