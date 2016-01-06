#!/usr/bin/python
# coding: utf-8

import random
import unittest
import time

"""
快排，速度shua shua 的
"""


def time_it(func):
    def wrapper(*args, **kwargs):
        try:
            start = time.clock()
            return func(*args, **kwargs)
        finally:
            end = time.clock()
            print 'using time: %s' % (end-start)
    return wrapper


def bubble_sort(ul, lo, hi):
    "[lo, hi)"
    length = hi - lo
    if length < 2:
        return
    for i in range(length-1):
        for j in range(lo, hi-1-i):
            if ul[j] > ul[j+1]:
                ul[j], ul[j+1] = ul[j+1], ul[j]


def quickSort(ul): # 当>1000个时，出现错误根据数据不同,耗时幅度大,但是一般蛮小的.
    if len(ul) < 2: 
        return ul
    pivot = ul[0]
    left = [i for i in ul if i < pivot]
    mid = [i for i in ul if i == pivot]
    right = [i for i in ul if i > pivot]
    return quickSort(left) + mid + quickSort(right)


def qSort(ul):  # 当>1000个时，出现错误
    if len(ul)<2:
        return ul   
    i = 0
    pivot = ul[0]
    for j in range(1,len(ul)):
        if ul[j] <= pivot:
            i+= 1
            ul[i], ul[j] = ul[j], ul[i]
    ul[0],ul[i] = ul[i], ul[0]
    left = ul[:i]
    right = ul[i+1:]
    return qSort(left)+[pivot]+qSort(right)

# 固定选择
def quick_sort(array, lo, hi):
    """[lo, hi)"""
    if hi-lo < 6:
        bubble_sort(array, lo, hi)
        return
    else:
        pos = random.randint(lo, hi-1)
        array[lo],array[pos] = array[pos], array[lo]
        partition = array[lo]
        i = lo + 1
        j = hi
        while i < j:
            if array[i] <= partition:
                i += 1
            else:
                array[i], array[j-1] = array[j-1], array[i]
                j -= 1
                
        array[lo], array[i-1] = array[i-1], array[lo]
        quick_sort(array, lo, i-1)
        quick_sort(array, i, hi)


def quick_sort1(array, lo, hi):
    """[lo, hi)"""
    if lo < hi-1:
        partition = array[lo]
        i = lo + 1
        j = hi
        while i < j:
            if array[i] <= partition:
                i += 1
            else:
                array[i], array[j-1] = array[j-1], array[i]
                j -= 1
                
        array[lo], array[i-1] = array[i-1], array[lo]
        quick_sort1(array, lo, i-1)
        quick_sort1(array, i, hi)


def mergeSort(ul):
    if len(ul) < 2:
        return ul
    mid = len(ul)/2
    left = ul[0:mid]
    right = ul[mid:len(ul)]
    sorted_left = mergeSort(left)
    sorted_right = mergeSort(right)
    return merge(sorted_left, sorted_right)

def merge(left, right):
    ans = []
    while left and right:
        if left[0] <= right[0]:
            ans.append(left.pop(0))
        else:
            ans.append(right.pop(0))
    ans.extend(left)
    ans.extend(right)
    return ans
        

class QuickSortTest(unittest.TestCase):
    def testquick_sort(self):
        a1 = [2,2,2,1]
        print 'start: %r' % a1
        quick_sort(a1,0,len(a1))
        print 'after: %r' % a1
        self.assertEqual(a1, sorted(a1))
        
    def testmerge_sort(self):
        a2 = [2,2,2,1]
        print 'start: %r' % a2
        a3 = mergeSort(a2)
        print 'after: %r' % a3
        self.assertEqual(a3, sorted(a2))
        

if __name__ == '__main__':
    # unittest.main()
    l = range(10799,0,-1)
    l1 = range(10799,0,-1)
    l2 = range(10799,0,-1)
    
    s1 = time.clock()
    quick_sort(l1,0,10799)
    e1 = time.clock()
    print u'快速排序n logn版本用时:', e1-s1
    
    s2 = time.clock()
    b = mergeSort(l2)
    e2 = time.clock()
    print u'归并排序n logn版本用时:', e2-s2

    print l1 == sorted(l)
    print b == sorted(l2)

