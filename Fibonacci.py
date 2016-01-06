
def fun2(num):
    n,a,b = 0,0,1
    while n<num:
        print(b)
        a, b = b, b+a
        n += 1
    return 'done!'
fun2(44)

def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a


class Fib():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a>1000:
            raise StopIteration()
        return self.a

