import time
import bubbleSort
import mergeSort
import insertionSort
import selectionSort
import getrandata
import quickSort
import shellSort

data1 = getrandata.getrandata(10000)
data0 = data1[:]
data2 = data1[:]
data3 = data1[:]
data4 = data1[:]
data5 = data1[:]
data6 = data1[:]
data7 = data1[:]
data8 = data1[:]

s0 = time.clock()
data1.sort()
e0 = time.clock()
print 'The python sorted:', e0-s0

s7 = time.clock()
shellSort.shellSort(data7)
e7 = time.clock()
print 'shellSort:', e7-s7

s1 = time.clock()
mergeSort.mergeSort(data1)
e1 = time.clock()
print 'mergeSort:', e1-s1

s5 = time.clock()
quickSort.quick_sort(data5,0,len(data5))
e5 = time.clock()
print 'quick_sort:', e5-s5

s6 = time.clock()
quickSort.qSort(data6)
e6 = time.clock()
print 'qSort:', e6-s6

s3 = time.clock()
insertionSort.insertionSort(data3)
e3 = time.clock()
print 'insertionSort:', e3-s3

s8 = time.clock()
insertionSort.insertSort(data8, 0, len(data8))
e8 = time.clock()
print 'insertSort:', e8-s8


s4 = time.clock()
selectionSort.selectionSort(data4)
e4 = time.clock()
print 'selectionSort:', e4-s4

s2 = time.clock()
bubbleSort.bubble_sort(data2, 0, len(data2))
e2 = time.clock()
print 'bubble_sort:', e2-s2

