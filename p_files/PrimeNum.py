# -*- coding: cp936 -*-
count = 0
for i in range(2,101):
    for j in range(2,i):
        if i%j == 0:
            #print i,"is not prime number"
            break #找到能整除的，终止j的循环，由于break终止，不执行else，然后i+1
    else:         #j循环正常结束，执行else语句
        print i,"is a prime number"
        count += 1
print 'the number of prime number in 2-100 is',count

i= 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break  #找到一个能整除的，终止最近的while循环，\
      j = j + 1           #执行if,发现不满足条件，执行i+1
   if (j > i/j) : print i, " is prime number"
   i = i + 1

print "Good bye!"
       
