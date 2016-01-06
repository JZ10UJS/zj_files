#!/usr/bin/python
# coding:utf-8
# 冒泡排序
import time
import quickSort

def bubbleSort(uslist):
    count = 0
    length = len(uslist)
    for i in range(length-1):  # 此处-1，是减去  还剩最后一个数字没排序 的情况
        for j in range(0,length-1-i):
            count += 1
            if uslist[j] > uslist[j+1]:
                uslist[j], uslist[j+1] = uslist[j+1], uslist[j]
    return uslist,count 

def bubbleSort1(uslist):
    count = 0
    length = len(uslist)
    for i in range(length-1):       
        for j in range(0,length-1): # 与上个相比，此处没有 -i
            count += 1
            if uslist[j] > uslist[j+1]:
                uslist[j], uslist[j+1] = uslist[j+1], uslist[j]
    return uslist,count

if __name__ == '__main__':
    
    l1 = [26, 33, 57, 22, 7, 47, 76, 68, 51, 32, 93, 15, 71, 64, 10, 17, 90, 88, 8, 94, 80, 57, 55, 99, 11, 53, 93, 70, 90, 91, 38, 5, 30, 85, 18, 19, 42, 5, 48, 9, 53, 29, 54, 22, 53, 23, 84, 19, 80, 68, 38, 35, 52, 21, 34, 47, 46, 38, 41, 45, 27, 41, 35, 92, 4, 11, 21, 7, 7, 70, 67, 56, 63, 41, 11, 51, 12, 49, 47, 14, 46, 74, 27, 28, 92, 7, 82, 72, 18, 72, 80, 34, 83, 52, 85, 47, 46, 40, 83, 4]
    l2 = range(1000,0,-1)
    l3 = range(1000,0,-1)
    l4 = range(1000,0,-1)
    l5 = range(1000,0,-1)
    
    s = time.clock()
    bubbleSort(l3)
    e1 = time.clock()
    print u'冒泡排序n**2/2版本用时:', e1-s

    s1 = time.clock()
    bubbleSort1(l2)
    e2 = time.clock()
    print u'冒泡排序n**2/2版本用时:', e2-s1

    s2 = time.clock()
    quickSort.quick_sort(l4,0,len(l4))
    e3 = time.clock()
    print u'快速排序n logn版本用时:', e3-s2

    s3 = time.clock()
    b = quickSort.qSort(l5)
    e4 = time.clock()
    print u'快速排序n logn版本用时:', e4-s3


    
