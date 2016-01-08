import time
start = time.time()

def fun1(a,b):
    for i in a:
        if i not in b:
            return False
    return True
str1 = '0123456789'
count = 0
for i in range(203,987):
    for j in range(203,987):
        sumall = i + j
        if sumall>1000:
            l = str(sumall)+str(i)+str(j)
            if fun1(str1,l):
                print i,'+',j,'=',sumall
                count += 1
   
end = time.time()

print count
print end-start

        
