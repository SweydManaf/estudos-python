def count():
    i = 0
    while True:
        yield i
        i += 1

c = count()

mults1 = [next(c)*10 for x in range(10)]
mults2 = [next(c)*10 for x in range(10)]
