def genPrimes():
    b = 2
    primelist = []
    while 1:
        for i in primelist:
            if (b % i) == 0:
                b += 1
                break
        else:
            primelist.append(b)
            yield b
            b += 1
