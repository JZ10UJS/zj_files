#!usr/bin/python
# coding:utf-8
def countPrimes(n):
    if n < 3:
        return 0
    table = [True for i in range(n)]
    table[0] = False
    table[1] = False
    for i in range(2, n/2+1):
        if table[i]:
            table[i*i:n:i] = [False]*len(table[i*i:n:i])

    return sum(table)

print countPrimes(15)
