#!usr/bin/python
# coding: utf-8

import time

l = range(10000000)
l1 = range(1000000)
l2 = range(100000)

s = time.clock()
l.insert(0,l.pop(0))
e = time.clock()
print u'10,000,000 pop(0) 耗时:', e-s

s1 = time.clock()
l1.insert(0,l.pop(0))
e1 = time.clock()
print u'1,000,000 pop(0) 耗时:', e1-s1

s2 = time.clock()
l2.insert(0,l.pop(0))
e2 = time.clock()
print u'100,000 pop(0) 耗时:', e2-s2
