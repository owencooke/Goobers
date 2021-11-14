# TESTING
import pandas
from time import sleep
import yfinance as yf
import numpy as np

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

print(len(exp_mvas1))
print(len(exp_mvas2))
print(len(simple_mvas1))
print(len(simple_mvas2))
inter1 = [] # list of tuples to contain days b/w which an intersection occurs such that exp_mvas is increasing
inter2 = [] # list of tuples to contain days b/w which an intersection occurs such that simple_mvas is increasing

intra1 = []
intra2 = []

#print(exp_mvas)
#print(simple_mvas)

#############################################################################################################

g = [len(simple_mvas2),len(simple_mvas1)]
k = [len(exp_mvas2),len(exp_mvas1)]

lowg = g.sort()
lowk = k.sort()
print(g)
print(k)

for i in range(g[0]-1):
     if simple_mvas1[i]>simple_mvas2[i] and simple_mvas1[i+1]<simple_mvas2[i+1]:
         inter1.append((i,i+1))
     if simple_mvas1[i]<simple_mvas2[i] and simple_mvas1[i+1]>simple_mvas2[i+1]:
         inter2.append((i,i+1))

for i in range(k[0]-1):
     if exp_mvas1[i]>exp_mvas2[i] and exp_mvas1[i+1]<exp_mvas2[i+1]:
         intra1.append((i,i+1))
     if exp_mvas1[i]<exp_mvas2[i] and exp_mvas1[i+1]>exp_mvas2[i+1]:
         intra2.append((i,i+1))


print("simple intersections, lower interval increasing")
print(inter1)
print("simple intersentions, larger interval increasing")
print(inter2)
print("exp intersections, lower interval increasing")
print(intra1)
print("exp intersentions, larger interval increasing")
print(intra2)




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



