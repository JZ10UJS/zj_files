#!usr/bin/python
# coding: utf-8
# 希尔排序
#
from insertionSort import insertSort

def shellSort1(ul):
    length = len(ul)
    w = 0
    while w < length/3: # 步长H采用 Knuth提出的: 1 4 13 40  --- 即 i*3 + 1
        w = w*3 + 1     # 选出小于length的最大步长
    while w > 0:
        if length%w == 0:
            height = length / w
        else:
            height = length/w + 1
        for i in range(w):
            l = []
            for j in range(height):
                if i+w*j < length:
                    l.append(ul[i+w*j])
            newl = insertSort(l)
            for k in range(len(newl)):
                if i+k*w < length:
                    ul[i + k*w] = newl[k]
        w = (w-1)/3
    return ul

def shellSort(arr):
    dist = 0
    while dist < len(arr)/3:
        dist = dist*3 + 1      
    while dist>0:  
        for i in range(dist,len(arr)):  
            tmp = arr[i]  
            j = i  
            while j>=dist and tmp<arr[j-dist]:  
                arr[j] = arr[j-dist]  
                j -= dist  
            arr[j] = tmp  
        dist = (dist-1)/3
    return arr

if __name__ == '__main__':
    l = [10,2,1,3,9,8,4,6,5,7]
    print shellSort(l)
