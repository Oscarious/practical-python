# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_first_year = 1000
mounth = 1

while principal > 0:
    principal = principal * (1+rate/12) - payment - extra_payment_first_year
    total_paid = total_paid + payment
    mounth += 1
    if mounth > 12:
        extra_payment_first_year = 0

print('Total paid:', total_paid, ' over:', mounth, 'months')
