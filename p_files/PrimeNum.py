# -*- coding: cp936 -*-
count = 0
for i in range(2,101):
    for j in range(2,i):
        if i%j == 0:
            #print i,"is not prime number"
            break #�ҵ��������ģ���ֹj��ѭ��������break��ֹ����ִ��else��Ȼ��i+1
    else:         #jѭ������������ִ��else���
        print i,"is a prime number"
        count += 1
print 'the number of prime number in 2-100 is',count

i= 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break  #�ҵ�һ���������ģ���ֹ�����whileѭ����\
      j = j + 1           #ִ��if,���ֲ�����������ִ��i+1
   if (j > i/j) : print i, " is prime number"
   i = i + 1

print "Good bye!"
       
