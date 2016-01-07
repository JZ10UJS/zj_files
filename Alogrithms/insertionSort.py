#!/usr/bin/python
# coding: utf-8

import time
import random

"""
插入排序
时间 n -> n**2
"""


def insertionSort(uslist):
    """
    新增列表slist，将uslist.pop(1)与slist元素比较，若<,则插入,break。elif
    uslist为 全逆序时, 达到O(n)
    """
    if len(uslist) < 2:return uslist
    slist = [uslist.pop(0)]
    while len(uslist) > 0: # uslist还有元素的话,就pop(0)
        num = uslist.pop(0)
        for j in range(len(slist)): # 和sorted部分的前面比较, 再依次往后. 
            if num < slist[j]:    # 找个第一个比num大的，就插入，然后break 小循环
                slist.insert(j, num)
                break
            elif num > slist[j] and j == len(slist)-1: # 这属于num大于所有slist的元素
                slist.append(num)

    return slist


def insertSort(ul, lo, hi):
    """
    与上一个不同的是, 没有新建一个list, 比较时,从后面往前面比较.
    ul 顺序对越多, 速度越快, shellsort 应该调用此种算法.
    """
    for i in range(lo+1, hi):    # 从第 lo+1 个元素开始，因为第 lo 个无需操作
        j = i
        while j > lo:
            if ul[j] < ul[j-1]:  # 先和sorted部分的 后面比较, 再依次往前
                ul[j], ul[j-1] = ul[j-1], ul[j]
                j -= 1
            else:
                break
                
                   

if __name__ == '__main__':
    l1 = [random.choice(range(1000)) for i in range(1000)]
    l2 = l1[:]

    s = time.clock()
    a = insertionSort(l1)
    e1 = time.clock()
    print u'插入排序用时:', e1-s
    
    s2 = time.clock()
    insertSort(l2, 0, len(l2))
    e2 = time.clock()
    print u'插入排序用时:', e2-s2



