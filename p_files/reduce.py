def f(n):
    if n>1:
        y=n*f(n-1)
    if n==1:
        y=1
    return y
print f(5)
print'#'*40


def fun(x,y):
    return x*y
l=range(1,6)
print l
print reduce(fun,l)
print'#'*40

f = lambda x,y:x*y
print reduce(f,l)
print'#'*40


print reduce(lambda x,y:x*y,l)
