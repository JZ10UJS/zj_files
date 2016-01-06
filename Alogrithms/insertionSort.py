#!usr/bin/python
# coding: utf-8
# 插入排序
# 时间 n -> n**2
import time
def insertionSort(uslist):
    """新增列表slist，将uslist.pop(1)与slist元素比较，若<,则插入,break。elif
        uslist为 全逆序时, 达到n
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

def insertSort(ul):# 与上一个不同的是, 没有新建一个list, 比较时,从后面往前面比较.
    """
    ul 顺序对越多, 速度越快, shellsort 应该调用此种算法.
    """
    if len(ul)<2:return ul
    for i in range(1, len(ul)):
        j = i
        while j > 0:
            if ul[i] >= ul[j-1]:  # 先和sorted部分的 后面比较, 在依次往前
                ul.insert(j, ul.pop(i))
                break
            else:
                j -= 1
        else:
            ul.insert(0, ul.pop(i))
    return ul
                
                   

if __name__ == '__main__':
    l1 = [26, 33, 57, 22, 7, 47, 76, 68, 51, 32, 93, 15, 71, 64, 10, 17, 90, 88, 8, 94, 80, 57, 55, 99, 11, 53, 93, 70, 90, 91, 38, 5, 30, 85, 18, 19, 42, 5, 48, 9, 53, 29, 54, 22, 53, 23, 84, 19, 80, 68, 38, 35, 52, 21, 34, 47, 46, 38, 41, 45, 27, 41, 35, 92, 4, 11, 21, 7, 7, 70, 67, 56, 63, 41, 11, 51, 12, 49, 47, 14, 46, 74, 27, 28, 92, 7, 82, 72, 18, 72, 80, 34, 83, 52, 85, 47, 46, 40, 83, 4]
    l2 = l1[:]
    l3 = range(10000,0,-1)
    l4 = l3[:]

    s = time.clock()
    insertionSort(l1)
    e1 = time.clock()
    print u'插入排序用时:', e1-s
    
    s2 = time.clock()
    insertSort(l2)
    e2 = time.clock()
    print u'插入排序用时:', e2-s2


