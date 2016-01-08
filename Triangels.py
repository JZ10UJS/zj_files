#!/usr/bin/python
# coding: utf-8


def triangles(num):
    a = [1]
    print a
    i = 0
    while i < num-1:
        b = []
        for j in range(len(a)+1):
            if j == 0 or j == len(a):
                b.append(1)
            else:
                b.append(a[j-1]+a[j])
        print b
        i += 1
        a = b

triangles(10)

'''
def triangles():
    a = [1];
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

o = triangles()
# 交互界面 使用next(o) 查询
'''
