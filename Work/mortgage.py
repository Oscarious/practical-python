# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
ori_payment = 2684.11
payment = ori_payment
total_paid = 0.0
month = 1
extra_payment_start_month = 5 * 12 + 1
extra_payment_end_month = extra_payment_start_month + 4 * 12
extra_payment = 1000


while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = ori_payment + extra_payment
    else:
        payment = ori_payment

    if payment-principal > 0.0001:
        payment = principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month, total_paid, principal)
    month += 1

print('Total paid:', total_paid, '\n month', month)
