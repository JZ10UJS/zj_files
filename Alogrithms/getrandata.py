import random

def getrandata(size):
    a = []
    i = 0
    while i < size:
        a.append(random.randrange(0, 1000000))
        i += 1
    return a

