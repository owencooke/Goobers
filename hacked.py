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

data = pandas.DataFrame(price_data, columns=['Date', 'Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume'])
print(data)