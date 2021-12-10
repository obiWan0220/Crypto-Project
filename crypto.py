
import finnhub
import pandas as pd
import datetime as dt
finnhub_client = finnhub.Client(api_key="c5k48vaad3ie96ef5i60")
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days=365)
end = int(end_date.timestamp())
start = int(start_date.timestamp())

finnhub_client = finnhub.Client(api_key="c5k48vaad3ie96ef5i60")
print(finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'M', start, end)) # Bitcoin
print(finnhub_client.crypto_candles('BINANCE:ETHUSDT', 'M', start, end)) # Etherum
print(finnhub_client.crypto_candles('BINANCE:SHIBUSDT', 'M', start, end,)) # Shibu Inu Coin
print(finnhub_client.crypto_candles('BINANCE:ADAUSDT', 'M', start, end,)) # cardono 
