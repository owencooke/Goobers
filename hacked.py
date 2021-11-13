'''
Title: HackedBeta Project
Contributors: Zamam Moeez, Jared Drueco, Aron Gu, Owen Cooke, Alina Iunusova
'''

# Project Ideas
# gpa calculator idk
# Predictions based on mathematical models
# perhaps load data as a text file, reading it shouldnt be too difficult

import pandas

price_data = pandas.read_excel('oil_prices.xlsx', sheet_name = 'Sheet1')
price_data = price_data[price_data.Volume != '-']
price_data.to_csv(index=False)

data = pandas.DataFrame(price_data, columns=['Date', 'Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume'])
print(data)