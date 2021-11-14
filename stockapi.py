import pandas
from time import sleep
from pandas.io.parsers import read_csv
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


# Get stock code and period
stock = str(input('Please name the stock code:  '))
period = str(input('What time interval do you want the prediction to be based on? (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max):  '))

stock_info = yf.Ticker('CL=F')   # Retrieves stock info
historical = stock_info.history(period=period)  # Historical data for a given period

# Display minimum and maximum closing prices of given time interval
print("Maximum Closing Price: {0}".format(round(max(historical.Close),2)))
print("Minimum Closing Price: {0}".format(round(min(historical.Close),2)))

# Display the table of the stock price data for a given time interval
print(historical)

# All the high column stock prices for a given time interval 
hig = historical[historical.columns[1]]
higlist = hig.to_numpy()

# All the low column stock prices for a given time interval
lowl = historical[historical.columns[2]]
lollist = lowl.to_numpy()

plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.plot(higlist, "-r", label='Highs')
plt.plot(lollist, "-b", label='Lows')
plt.title("Low and High Price Data for Stocks of "+ period + " Interval")
plt.legend()
plt.show()

close = historical[historical.columns[3]]

closelist = close.to_numpy()


# Simple Moving Average Based on User-Input
mva1 = int(input('What length of moving average would you like to apply? Enter an integer: '))
mva2 = int(input('Please enter a shorter moving average length, enter an integer: '))
simple_mvas1 = []
exp_mvas1 = []
simple_mvas2 =[]
exp_mvas2 =[]
smoothing1 = 2/(1+mva1)  # source for EMA formula: https://www.investopedia.com/terms/e/ema.asp
smoothing2 = 2/(1+mva2)

for i in range(mva1, len(closelist)+1):
	simple_mvas1.append(sum(closelist[(i-mva1):i])/mva1)

for i in range(mva2, len(closelist)+1):
	simple_mvas2.append(sum(closelist[(i-mva2):i])/mva2)

# Exponential Moving Average Based on User-Input
exp_mvas1.append(closelist[0])
for i in range(1, len(closelist)):
		exp_mvas1.append(closelist[i]*smoothing1 + exp_mvas1[i-1]*(1-smoothing1))  # see above source

exp_mvas2.append(closelist[0])
for i in range(1, len(closelist)):
		exp_mvas2.append(closelist[i]*smoothing2 + exp_mvas2[i-1]*(1-smoothing2))

inter1 = [] # list of tuples to contain days b/w which an intersection occurs such that simple_mvas1 is decreasing
inter2 = [] # list of tuples to contain days b/w which an intersection occurs such that simple_mvas1 is increasing

intra1 = [] # list of tuples to contain days b/w which an intersection occurs such that exp_mvas1 is decreasing
intra2 = [] # list of tuples to contain days b/w which an intersection occurs such that exp_mvas2 is decreasing

# Tuples that store the length of datasets for the 2 simple moving averages and 2 exponential moving averages
g = [len(simple_mvas2),len(simple_mvas1)]
k = [len(exp_mvas2),len(exp_mvas1)]
lowg = g.sort()
lowk = k.sort()

# Find intersections of the 2 simple moving average graphs based on the graphs increasing/decreasing
for i in range(g[0]-1):
     if simple_mvas1[i]>simple_mvas2[i] and simple_mvas1[i+1]<simple_mvas2[i+1]:
         inter1.append((i,i+1))
     if simple_mvas1[i]<simple_mvas2[i] and simple_mvas1[i+1]>simple_mvas2[i+1]:
         inter2.append((i,i+1))

# Find intersections of the 2 exponential moving average graphs based on the graphs increasing/decreasing
for i in range(k[0]-1):
     if exp_mvas1[i]>exp_mvas2[i] and exp_mvas1[i+1]<exp_mvas2[i+1]:
         intra1.append((i,i+1))
     if exp_mvas1[i]<exp_mvas2[i] and exp_mvas1[i+1]>exp_mvas2[i+1]:
         intra2.append((i,i+1))

# Output intervals of increase/decrease along with intersections of the exponential and simple moving averages
print("simple intersections, lower interval increasing")
print(inter1)
print("simple intersentions, larger interval increasing")
print(inter2)
print("exp intersections, lower interval increasing")
print(intra1)
print("exp intersentions, larger interval increasing")
print(intra2)

# Determines whether stock should be bought/sold based on the simple model
if simple_mvas1[-1]<simple_mvas2[-1]:
    print("You should buy the stock based on the simple model.")
if simple_mvas1[-1]>simple_mvas2[-1]:
    print("You should sell the stock based on the simple model.")

# Determines whether stock should be bought/sold based on the simple model
if exp_mvas1[-1]<exp_mvas2[-1]:
    print("You should buy the stock based on the exponential model.")
if exp_mvas1[-1]>exp_mvas2[-1]:
    print("You should sell the stock based on the exponential model.")

days = list(range(0, len(closelist)))
plt.plot(days, closelist,'k-', label='Closing Prices')
plt.plot(simple_mvas1, 'r--', label='Simple ' + str(mva1) + '-Day Moving Average')
plt.plot(exp_mvas1, 'g-', label='Exponential ' + str(mva1) + '-Day Moving Average')
plt.plot(simple_mvas2, 'b--', label='Simple ' + str(mva2) + '-Day Moving Average')
plt.plot(exp_mvas2, 'y-', label='Exponential ' + str(mva2) + '-Day Moving Average')
plt.ylabel('Price ($)')
plt.xlabel('Days')
plt.legend()
plt.title(stock + ' Stock - Period: ' + period + ' (source: YahooFinance)')
plt.show()







