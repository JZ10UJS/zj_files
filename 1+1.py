import time
import math
st = time.clock()
def isPrime(n):
    global i
    for i in range(3,int(math.sqrt(n)),2):
        if n%i == 0:
            return False
    return True
end = time.clock()
print(isPrime(1234567811),i,end-st)
'''num = int(input('num = :'))
count = 0
for num1 in range(2,num//2+1):
    if isPrime(num1):
        num2 = num - num1
        if isPrime(num2):
            print('%s = %s + %s' % (num,num1,num2))
            break

sum1 = 0
for i in range(2,10**4):
    if (isPrime(i)):
        sum1 += i
'''
