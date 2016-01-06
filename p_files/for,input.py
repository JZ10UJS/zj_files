def fun(x,y):
    #num = 0
    #for i in range(x,y):
    #    num = num + i
    #return num
    return sum(range(x,y))
    
a = int(raw_input('input the min num:'))
b = int(raw_input('input the max num:'))

print 'the answer is:',fun(a,b) 
    
