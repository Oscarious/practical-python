# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    f = open(filename, 'rt')
    total_cost = 0
    for line in f:
        row = line.split(',')
        try:
            total_cost += int(row[1]) * float(row[2])
        except ValueError as e:
            print("WARNING: field not match or missing")
            pass
    return total_cost
total_cost = portfolio_cost(sys.argv[1])
print(f'total cost: {total_cost}')