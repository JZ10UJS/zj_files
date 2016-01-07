#!/usr/bin/python
# coding:utf-8
# 选择排序

def selectionSort(ul, lo, hi):
    """
    [lo, hi)
    外面len(uslist)-1次大循环，内部小循环标记出未排序部分的最大值。
    和泡一样 O(n**2), 减少了交换次数
    """
    for i in range(hi-lo-1):  # -1是最后剩一个的时候，直接忽略
        mark = ul[lo]
        for j in range(lo, hi-i):
            if ul[j] >= mark:
                mark = ul[j]
                posi = j
        ul[posi], ul[j] = ul[j], ul[posi]

if __name__ == '__main__':
    l = [10,3,2,8,1,5,4,9,7,6,1]
    selectionSort(l, 0, len(l))
    print l
