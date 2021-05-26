# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                nshares = int(row[1])
                price = float(row[2])
                holding = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
                portfolio.append(holding)
    return portfolio

def read_prices(filename):
    res = {}
    with open('Data/prices.csv', 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            if (len(row) > 1):
                res[row[0]] = float(row[1])
    return res