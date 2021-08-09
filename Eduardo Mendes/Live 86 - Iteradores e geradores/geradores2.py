def contador():
    index = 0
    while True:
        yield index
        index += 1


c = contador()
for n in range(6):
    #print(next(c))
    ...

# < -------------------------------------------- >

def multiplipo(valor, inicio=1):
    while True:
        yield valor * inicio
        inicio += 1

pa = multiplipo(5, 2)

for n in range(5):
    print(next(pa))