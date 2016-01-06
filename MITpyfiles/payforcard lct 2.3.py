#!usr/bin/python
# -*- utf-8 -*-
balance = 999999
annualInterestRate = 0.2
MonIntRate= annualInterestRate / 12.0

lo = balance / 12.0
hi = (balance*(1+MonIntRate)**12)/12.0
MinMonPay = (lo+hi)/2

while(abs(balance) > 0.01):
    balance = 320000
    for i  in range(12):
        balance = (balance - MinMonPay)*(1+MonIntRate)
    if balance > 0.01:
        lo = MinMonPay
        MinMonPay = (lo+hi)/2
    else:
        hi = MinMonPay
        MinMonPay = (lo+hi)/2
    
print balance, MinMonPay
