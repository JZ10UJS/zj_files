def triangles():
    a = [1];
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

o = triangles()
