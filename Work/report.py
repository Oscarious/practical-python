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
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
    return portfolio

# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         print("error")
#         exit()
#     read_partfolio(sys.argv[1])
