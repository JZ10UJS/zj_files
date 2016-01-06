def fun(a,b,n):
    for i in range(n):
        for j in range(n):
            if i*a + j*b == n:
                print i,j
                return True
    return False

