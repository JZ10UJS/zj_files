'''sum = 0
n = int(input('n =:'))
for i in range(1,n+1):
    sum += i*(i+1)
print(sum)
'''
def fun(n):
    if n < 1:
        return 1
    else:
        return n*fun(n-1)
print(fun(0))
