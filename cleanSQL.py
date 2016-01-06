#!usr/bin/python
# coding:utf-8

f = open('d:/zj.sql','r')
res = []
for line in f.readlines():
    line = line.strip()
    if  not len(line) or line.startswith('LOCK TABLE'):
        continue
    res.append(line)

open('d:/1.sql','w').write('%s' % '\n'.join(res))
