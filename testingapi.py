
from time import sleep
import yfinance as yf

sleep(1)

stock = str(input('Please name the stock code:  '))
period = str(input('What time interval do you want the prediction to be based on? (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max):  '))

stock_info = yf.Ticker(stock)
historical = stock_info.history(period="period")

#print(historical)

n = historical[-1]
