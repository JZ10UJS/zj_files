'''
def Hailstone(n):
    global l1,count
    l1.append(n)
    if n == 1:
        count += 1
    elif n%2 == 0:
        count += 1
        return Hailstone(n//2)
    else:
        count += 1
        return Hailstone(3*n+1)
l1 = []
count = 0
Hailstone(27)
print(l1,count)
'''

def hailstone(n):
    count1 = 1
    while n>1:
        l2.append(n)
        if n%2:
            n = 3*n+1
        else:
            n //= 2
        count1 +=1
    l2.append(1)
    return count1
l2 = []
print(hailstone(128918), l2)
