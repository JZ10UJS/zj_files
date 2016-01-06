def fun1(num, a, b, c):
    if(num == 1):
        print (a,'-->',c)
    else:
        fun1(num-1, a, c, b)
        print(a,'-->',c)
        fun1(num-1, b, a, c)

fun1(5,'A','B','C')
