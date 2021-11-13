
from time import sleep
import yfinance as yf
sleep(1)

stock = str(input('Please name the stock code:  '))

stock_info = yf.Ticker(stock)
historical = stock_info.history(period="max")

print(historical)

