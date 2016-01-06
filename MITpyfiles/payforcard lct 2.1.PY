#! usr/bin/python
# -*- coding: utf-8 -*-

blc = 4842   #欠款
annualInterestRate = 0.2    #年利率
monthlyPaymentRate = 0.04   #每月最低偿还比例
MonIntRate= annualInterestRate / 12.0  #月利率

totalPaid = 0
for i in range(1,13):
    MinMonPay = blc * monthlyPaymentRate #minimum monthly payment
    blc = (blc - MinMonPay)*(1+MonIntRate) # Remaining balance本月末，下月初的余额。
    print 'Month:', i
    print 'Minimum monthly payment:', round(MinMonPay, 2)
    print 'Remaining balance:', round(blc, 2)
    totalPaid += MinMonPay

print 'Total paid:', round(totalPaid, 2)
print 'Remaining balance:', round(blc, 2)
