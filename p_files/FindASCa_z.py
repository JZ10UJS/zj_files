#coding:utf-8
import string
import re

s = string.ascii_lowercase # 生成a-z的字符串
count1 = 0
f1 = open('abc.txt','r')
code = f1.read()

for i in s:
    li = re.findall(i,code)# li找到的i的序列
    count1 = len(li)
    print count1,i,'has been found'

print '\n\n\n'

l_code = list(code)
for j in s:
    count2 = l_code.count(j)
    print count2,j,'has been found'

f1.close()

