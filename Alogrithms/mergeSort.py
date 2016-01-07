#!/usr/bin/python
# coding:utf-8
# 归并排序

import time
import random

"""
list1 = [1,3,5,7,9,10,11]  # mergeSort合并的主要算法
list2 = [2,4,6,8]
res = []
while len(list1)!=0 and len(list2)!=0:
    res.append(list1.pop(0)) if list1[0] <= list2[0] else res.append(list2.pop(0))
res += list1 + list2
print res
"""


def mergeSort(uslist):  #unsorted list
    if len(uslist) < 2:
        return uslist
    else:
        lo = 0
        hi = len(uslist)
        mid = (lo + hi)/2
        left = mergeSort(uslist[lo:mid])
        right = mergeSort(uslist[mid:hi])
        return merge(left, right)


def merge(list1, list2): # 将有序list1 和 有序list2 合并成 有序序列res,并返回。
    res = []
    while len(list1)!=0 and len(list2)!=0:
        res.append(list1.pop(0)) if list1[0] <= list2[0] else res.append(list2.pop(0))

    return res+list1+list2


if __name__ == '__main__':
    l1 = [random.randrange(0, 100) for i in range(100)]
    l2 = range(1000,0,-1)
    
    start = time.clock()
    mergeSort(l1)
    end = time.clock()
    print u'归并排序用时:',end-start

    s1 = time.clock()
    mergeSort(l2)
    s2 = time.clock()
    print u'归并排序用时',s2-s1
