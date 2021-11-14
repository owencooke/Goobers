# TESTING
import pandas
from time import sleep
import yfinance as yf

sleep(1)

#get stock code and period
stock = str(input('Please name the stock code:  '))
period = str(input('What time interval do you want the prediction to be based on? (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max):  '))

stock_info = yf.Ticker(stock)   #retrieves stock info
historical = stock_info.history(period=period)  #historical data for a given period
print(historical)




###########################################################################################
# Owen's Additions - add to testingapi.py
# No forecasting, but gives a simple/exponential moving average based on data

import matplotlib.pyplot as plt

close = historical[historical.columns[3]]

#print(close)

closelist = close.to_numpy()

#print(closelist)

# Simple Moving Average Based on User-Input
mva = int(input('What length of moving average would you like to apply? Enter an integer: '))
simple_mvas = []
exp_mvas = []
smoothing = 2/(1+mva)  # source for EMA formula: https://www.investopedia.com/terms/e/ema.asp

for i in range(mva, len(closelist)+1):
	simple_mvas.append(sum(closelist[(i-mva):i])/mva)

# Exponential Moving Average Based on User-Input
exp_mvas.append(closelist[0])
for i in range(1, len(closelist)):
		exp_mvas.append(closelist[i]*smoothing + exp_mvas[i-1]*(1-smoothing))  # see above source


days = list(range(0, len(closelist)))
plt.plot(days, closelist, label='Closing Prices')
plt.plot(simple_mvas, 'r-', label='Simple ' + str(mva) + '-Day Moving Average')
plt.plot(exp_mvas, 'g-', label='Exponential ' + str(mva) + '-Day Moving Average')
plt.ylabel('Price ($)')
plt.xlabel('Days')
plt.legend()
plt.title(stock + ' Stock - Period: ' + period + ' (source: YahooFinance)')
plt.show()

