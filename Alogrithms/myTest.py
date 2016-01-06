#!/usr/bin/python
# coding: utf-8

import random


def bubble_sort(ul, lo, hi):
    "[lo, hi)"
    if hi-lo <= 1:
        return
    for i in range(hi-lo-1):
        for j in range(lo, hi-1-i):
            if ul[j] > ul[j+1]:
                ul[j], ul[j+1] = ul[j+1], ul[j]


def quick_sort(ul, lo, hi):
    "[lo, hi)"
    if hi-lo <= 5:
        bubble_sort(ul, lo, hi)
        return

    pivot = ul[lo]
    i = lo + 1
    j = hi
    while i < j:
        if ul[i] <= pivot:
            i += 1
        else:
            ul[i], ul[j-1] = ul[j-1], ul[i]
            j -= 1

    ul[lo], ul[i-1] = ul[i-1], ul[lo]
    quick_sort(ul, lo, i-1)
    quick_sort(ul, i, hi)


if __name__ == '__main__':
    l = [random.choice(range(1000)) for i in range(100)]
    b = l[:]
    l1 = l[:]
    l2 = l[:]
    bubble_sort(l1, 0, len(l1))
    quick_sort(l2, 0, len(l2))
    print l1 == sorted(b)
    print l2 == sorted(b)
    
    
