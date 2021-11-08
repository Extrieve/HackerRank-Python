import requests
token = 'Tsk_1c42cee11b834d83b84aec96ae542f1a'
ticker = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{ticker}/quote/?token={token}'
## Transform the data as a json object
stock = requests.get(api_url).json()
print(stock['companyName'])

keys = ['avgTotalVolume', 'calculationPrice', 'change', 'changePercent', 'close', 'closeSource', 'closeTime', 'companyName', 'currency', 'delayedPrice', 'delayedPriceTime', 'extendedChange', 'extendedChangePercent', 'extendedPrice', 'extendedPriceTime', 'high', 'highSource', 'highTime', 'iexAskPrice', 'iexAskSize', 'iexBidPrice', 'iexBidSize', 'iexClose', 'iexCloseTime', 'iexLastUpdated', 'iexMarketPercent', 'iexOpen',
        'iexOpenTime', 'iexRealtimePrice', 'iexRealtimeSize', 'iexVolume', 'lastTradeTime', 'latestPrice', 'latestSource', 'latestTime', 'latestUpdate', 'latestVolume', 'low', 'lowSource', 'lowTime', 'marketCap', 'oddLotDelayedPrice', 'oddLotDelayedPriceTime', 'open', 'openTime', 'openSource', 'peRatio', 'previousClose', 'previousVolume', 'primaryExchange', 'symbol', 'volume', 'week52High', 'week52Low', 'ytdChange', 'isUSMarketOpen']
