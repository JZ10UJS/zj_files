import re
fp = file('test.txt','r')
count = 0
str1 = fp.read()

list1 = re.findall(r'hello',str1)

print len(list1)

fp.close()
