#!/usr/bin/python
# coding:utf-8
# 归并排序
import time
"""
list1 = [1,3,5,7,9,10,11]  # mergeSort合并的主要算法
list2 = [2,4,6,8]
res = []
while len(list1)!=0 and len(list2)!=0:
    res.append(list1.pop(0)) if list1[0] < list2[0] else res.append(list2.pop(0))
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
        res.append(list1.pop(0)) if list1[0] < list2[0] else res.append(list2.pop(0))
    return res+list1+list2

if __name__ == '__main__':
    l1 = [26, 33, 57, 22, 7, 47, 76, 68, 51, 32, 93, 15, 71, 64, 10, 17, 90, 88, 8, 94, 80, 57, 55, 99, 11, 53, 93, 70, 90, 91, 38, 5, 30, 85, 18, 19, 42, 5, 48, 9, 53, 29, 54, 22, 53, 23, 84, 19, 80, 68, 38, 35, 52, 21, 34, 47, 46, 38, 41, 45, 27, 41, 35, 92, 4, 11, 21, 7, 7, 70, 67, 56, 63, 41, 11, 51, 12, 49, 47, 14, 46, 74, 27, 28, 92, 7, 82, 72, 18, 72, 80, 34, 83, 52, 85, 47, 46, 40, 83, 4]
    l2 = range(1000,0,-1)
    
    start = time.clock()
    mergeSort(l1)
    end = time.clock()
    print u'归并排序用时:',end-start

    s1 = time.clock()
    mergeSort(l2)
    s2 = time.clock()
    print u'归并排序用时',s2-s1
