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