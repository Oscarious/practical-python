# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
total_cost = 0
for line in f:
    row = line.split(',')
    try:
        total_cost += int(row[1]) * float(row[2])
    except ValueError as e:
        pass
print(f'total cost: {total_cost}')