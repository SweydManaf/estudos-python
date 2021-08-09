def geradora():
    yield 'A'
    yield 'B'
    yield 'C'

g = geradora()

print(next(g), next(g), next(g))