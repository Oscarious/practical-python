# pcost.py
#
# Exercise 1.27
import sys
import csv
import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

if len(sys.argv) == 2:
    filename = sys.argv[1]
    cost = portfolio_cost(sys.argv[1])
    print('Total cost:', cost)
else:
    filename = input('Enter a filename:')
