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

def cal_profit():
    portfolios = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    profit = 0
    for portfolio in portfolios:
        profit = portfolio['shares'] * (prices[portfolio['name']]-portfolio['price'])
    return profit

def make_report(portfolio, prices):
    report = []
    for item in portfolio:
        price = prices[item['name']]
        report.append((item['name'], item['shares'], price, price-item['price']))
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    split_line = ('----------', '----------', '----------', '----------')
    print('%10s %10s %10s %10s' % headers)
    print('%10s %10s %10s %10s' % split_line)
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)