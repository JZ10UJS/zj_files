balance = 3329
annualInterestRate = 0.2
MonIntRate= annualInterestRate / 12.0

MinMonPay = 200

while(balance >0):
    balance = 4773
    MinMonPay += 10
    for i  in range(12):
        balance = (balance - MinMonPay)*(1+MonIntRate)
print balance, MinMonPay
