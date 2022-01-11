import requests
import ssl
s = requests.Session()
s.verify = False
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

token = 'Tsk_c680c72f0f63469cbce56795e7713af9'
ticker = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{ticker}/quote/?token={token}'
# api_url = f'https://sandbox.iexapis.com/stable/stock/aapl/chart/20200415?token={token}'


## Transform the data as a json object
myrequest = s.get(api_url)
stock = myrequest.json()
print(stock)
# print(stock['companyName'])

historical_keys = ['close', 'high', 'low', 'open', 'symbol', 'volume', 'id', 'key', 'subkey', 'date', 'updated', 'changeOverTime', 'marketChangeOverTime',
                   'uOpen', 'uClose', 'uHigh', 'uLow', 'uVolume', 'fOpen', 'fClose', 'fHigh', 'fLow', 'fVolume', 'label', 'change', 'changePercent']

# for data in stock:
#     print(f"{data['close']} {data['volume']} {data['date']}")

keys = ['avgTotalVolume', 'calculationPrice', 'change', 'changePercent', 'close', 'closeSource', 'closeTime', 'companyName', 'currency', 'delayedPrice', 'delayedPriceTime', 'extendedChange', 'extendedChangePercent', 'extendedPrice', 'extendedPriceTime', 'high', 'highSource', 'highTime', 'iexAskPrice', 'iexAskSize', 'iexBidPrice', 'iexBidSize', 'iexClose', 'iexCloseTime', 'iexLastUpdated', 'iexMarketPercent', 'iexOpen',
        'iexOpenTime', 'iexRealtimePrice', 'iexRealtimeSize', 'iexVolume', 'lastTradeTime', 'latestPrice', 'latestSource', 'latestTime', 'latestUpdate', 'latestVolume', 'low', 'lowSource', 'lowTime', 'marketCap', 'oddLotDelayedPrice', 'oddLotDelayedPriceTime', 'open', 'openTime', 'openSource', 'peRatio', 'previousClose', 'previousVolume', 'primaryExchange', 'symbol', 'volume', 'week52High', 'week52Low', 'ytdChange', 'isUSMarketOpen']

# print(historical)
