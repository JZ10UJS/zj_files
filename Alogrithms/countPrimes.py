#!/usr/bin/python
# coding:utf-8


def countPrimes(n):
    if n < 2:
        return 0
    table = [True for i in range(n)]
    table[0] = False
    table[1] = False
    for i in range(2, int(n**0.5)+1):
        if table[i]:
            table[i*i:n:i] = [False] * len(table[i*i:n:i])

    return sum(table)


def genPrimes():
    test_num = 2               # 从2开始生成
    primelist = []             # 初始化素数表，空
    while 1:                   # 一直这么生产下去
        for i in primelist:
            if (test_num % i) == 0: 
                test_num += 1  # 如果此数字，能被素数表中某数整除，换到下一个数字
                break          # break 掉 for 循环
        else:
            primelist.append(test_num)  # 当该数字不能被素数表中的数整除，for循环
            yield test_num              # 正常结束，进入 else 语句，将其加入素数表
            test_num += 1               # yield 出去， 下次调用时，换到下一个数字
            

if __name__ == '__main__':
    print countPrimes(100)
    b = genPrimes()
    i = 0
    while i < 25:
        print b.next()
        i += 1
