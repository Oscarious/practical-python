# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    total_cost = 0
    for rowno, row in enumerate(rows, start=1):
        try:
            total_cost += int(row[1]) * float(row[2])
        except ValueError as e:
            print('Row {}: Bad row: {}'.format(rowno, row))
    return total_cost