def fun1(num, a, b, c):
    while num == 1:
        print (a,'-->',c)
        break
    fun1(num-1, a, c, b)
    print(a,'-->',c)
    fun1(num-1, b, a, c)

fun1(3,'A','B','C')
