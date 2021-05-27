# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    total_cost = 0
    headers = next(rows)
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total_cost += nshares * price
        except ValueError as e:
            print('Row {}: Bad row: {}'.format(rowno, row))
    return total_cost