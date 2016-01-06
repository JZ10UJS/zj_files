import math
def f(x):
    return 10*math.e**(math.log(0.5)/5.27*x)
def radiationExposure(start, stop, step):
    sum1 = 0
    while start < stop:
        sum1 += step * f(start)
        start += step
    return sum1

