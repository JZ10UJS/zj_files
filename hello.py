p = 'eehhh'
t = 'skeeehhhjasjfaieo oiafml ; fjfsadfeo heyllo'
n = len(t)
m = len(p)
i,j=0,0
while(j<m and i<n):
    if(t[i] == p[j]):
        i += 1
        j += 1
    else:
        i -= j-1 #假如 i j 前两个都相等，第三个不等，意味着下一次的i = i+1 -j
        j = 0
print(i-j) #返回找到的位置  算法O(mn)

