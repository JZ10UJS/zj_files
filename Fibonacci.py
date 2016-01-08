#!/usr/bin/python
# coding: utf-8


def fun2(num):
    n,a,b = 0,0,1
    while n<num:
        print a
        a, b = b, b+a
        n += 1
    return 'done!'


def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a


class Fib():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a>1000:
            raise StopIteration()
        return self.a


if __name__ == '__main__':
    fun2(10)
    for i in range(10):
        print fib(i)

