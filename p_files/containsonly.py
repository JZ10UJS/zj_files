def fun1(a,b):
    for i in a:
        if i not in b:
            return False
    return True
    '''for k in a:
        if k not in b:
            return 0
        return 1'''

str1 = '0123456789'
s = '1234056789'

fun1(str1,s)
