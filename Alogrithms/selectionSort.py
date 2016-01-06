#!usr/bin/python
# coding:utf-8
# 选择排序

def selectionSort(uslist):
    """外面len(uslist)-1次大循环，内部小循环标记出未排序部分的最大值。
    和冒泡一样 O(n**2)"""
    hi = len(uslist)
    for i in range(0, len(uslist)-1):  # 此处减一 是减少最后还剩1个数没排序的情况
        lo = 0                         # 比如 3个数，外面只需要 套2个循环就行。
        mark = 0
        while lo < hi:                 # 未排序部分[lo, hi)内部一趟排序，选出最大数，标记mark
            if uslist[lo] >= uslist[mark]:  # 大于等于是为了算法的稳定性，即不改变相同数值的先后顺序
                mark = lo
            lo += 1    
        uslist[hi-1],uslist[mark] = uslist[mark], uslist[hi-1] #  让mark 和 uslist最后一个数 互换
        hi -= 1           #  此时，为排序的的部分 hi-1。

    return uslist


if __name__ == '__main__':
    l = [10,3,2,8,1,5,4,9,7,6]
    print selectionSort(l)
