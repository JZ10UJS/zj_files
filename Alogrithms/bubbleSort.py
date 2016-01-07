#!/usr/bin/python
# coding: utf-8

import time


def bubbleSort(uslist):
    length = len(uslist)
    for i in range(length-1):  # 此处-1，是减去  还剩最后一个数字没排序 的情况
        for j in range(0, length-1-i):
            if uslist[j] > uslist[j+1]:
                uslist[j], uslist[j+1] = uslist[j+1], uslist[j]


def bubbleSort1(uslist):
    length = len(uslist)
    for i in range(length-1):       
        for j in range(0, length-1): # 与上个相比，此处没有 -i
            count += 1
            if uslist[j] > uslist[j+1]:
                uslist[j], uslist[j+1] = uslist[j+1], uslist[j]

    
def bubble_sort(ul, lo, hi):
    "[lo, hi) 当然这个比较好咯"
    for i in range(hi-lo-1):
        for j in range(lo, hi-1-i):
            if ul[j] > ul[j+1]:
                ul[j], ul[j+1] = ul[j+1], ul[j]
