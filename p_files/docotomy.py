def fun1(x):
    return 3*(x**4)+6*x**3-123*x*x-126*x+1080
a = -10.0
b = 10.0
c = (a+b)/2
count = 0

while abs(fun1(c)) >0.001:
    count += 1
    if fun1(a)*fun1(c) < 0:
        b = c
        c = (a+c)/2
    else:
        a = c
        c = (b+c)/2
    
'''
while abs(fun1(c))>0.001:
    if fun1(c)>0:
        c = (a+c)/2
    else:
        c = (b+c)/2
'''
print c
print count
    
