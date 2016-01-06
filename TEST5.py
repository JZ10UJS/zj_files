def hanoii(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        hanoii(n-1,a,c,b)
        print(a,'-->',c)
        hanoii(n-1,b,a,c)

hanoii(3,'A','B','C')
