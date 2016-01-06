#!urs/bin/python
# coding:utf-8
"""为了算出1<=i<=10**12 的所有 d1(i) 之和
   还没弄出来。"""
def d1(n):
    """算出某个正整数的正约数之和
    公式基于 n可以被分解成 n = a1**p1 * a2**p2 * a3**p3
正约数之和=(a1的0次方加到a1的p1次方)*(a2的0次方加到a2的p2次方)*(a3的0次方加到a3的p3次方)"""
    i = 2
    count = 0
    res = 1
    res1 = 1
    while n>=i:
        if n%i == 0:
            count +=1
            n /= i
            res += i**count
        else:
            res1 *= res
            res = 1 
            count = 0
            i += 1
    return res1 * res

suma = 0
i = 1
print d1(200),d1(400),d1(2000)
