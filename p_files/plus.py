from itertools import permutations
import time
start = time.clock()

num = [0,2,3,4,5,6,7,8,9]

num_per = permutations(num, 9)

counter = 0
ok =[]

for vec in num_per:
    a,b,c,d,e,f,g,h,i= vec
    if a != 0 and d!=0:
        num1 = 100*a+10*b+c
        num2 = 100*d+10*e+f
        suma = 1000+100*g+10*h+i
        if num1+num2 == suma:
            counter +=1
            ok.append(vec)
            print counter,num1,'+',num2,'=',suma #这是输出有哪些数字符合要求

end = time.clock()
print end-start
print counter
