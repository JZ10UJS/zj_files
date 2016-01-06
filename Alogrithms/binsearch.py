#!usr/bin/python
# coding: utf-8

def binsearch(num, slist):  #sorted list
    """在一个有序的序列中，二分查找某个数。
       若这个数在序列中，返回他秩最大的那个秩（也等于 返回比它大的最小数的秩-1）
       若不在序列中，返回比他大的最小数的秩-1
       such as:
       binsearch(9,[1,3,5,9,9,10,11])  返回 10的秩-1，即5-1，为4
       binsearch(8,[1,3,5,9,9,10,11])  返回 第一个9的秩-1,即3-1 ，为2

       插入时算法，为了插入后，保持有序
       insert(search(num, slist)+1, num)  看清楚，有个+1"""
    lo = 0
    hi = len(slist)
    while lo < hi:
        mi = (lo+hi)>>1
        if num < slist[mi]:  # 想想这儿为什么不是 <=
            hi = mi
        else:
            lo = mi + 1      # 想想为什么不是 lo = mi, 为什么区间跳过了 mi
                             # 其实我们并不是找到num,而是找到比num大的最小数
                             # 所以，此时我们跳过的mi就是num.
    return lo-1



if __name__ == '__main__':
    print binsearch(9,[1,3,5,9,9,10,11])
    print binsearch(2,[1,3,5,9,9,10,11])
    
