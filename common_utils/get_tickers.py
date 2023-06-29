import requests


def get_tickers():

    url = "https://api.upbit.com/v1/market/all?isDetails=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    ticker_agg = response.json()
    krw_market, btc_market, usdt_market = {}, {}, {}

    for ticker_details in ticker_agg:

        market, ticker = ticker_details["market"].split("-")
        asset_name = ticker_details["english_name"].lower()

        data = {ticker: asset_name}

        if "KRW" in market:
            krw_market.update(data)
        
        elif "BTC" in market:
            btc_market.update(data)
        
        elif "USDT" in market:
            usdt_market.update(data)
    
    markets = {"krw": krw_market, "btc": btc_market, "usdt": usdt_market}
    
    return markets