#!/usr/bin/python
# coding: utf-8

"""
Hanoi Tower
"""

def hanoi(num, a, b, c):
    if(num == 1):
        print a,'-->',c
    else:
        hanoi(num-1, a, c, b)
        print a,'-->',c
        hanoi(num-1, b, a, c)


if __name__ == '__main__':
    hanoi(5,'A','B','C')
