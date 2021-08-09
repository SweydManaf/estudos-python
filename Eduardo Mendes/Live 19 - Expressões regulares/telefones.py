import re
from random import randint
from itertools import permutations

cel = re.compile(r'11[7-9][0-9]{7}')

for tel in permutations(range(0, 10), 10):
    _tel = ''.join(str(x) for x in tel)
    if cel.search(_tel):
        print(_tel)

# def genRandomNumbers(tamanho):
#     numero = ''
#     for x in range(tamanho):
#         numero += str(randint(0,9))
#     return numero
#
# def numeroValido():
#     num = genRandomNumbers(10)
#     if cel.search(num):
#         print(num)
#
# for i in range(1000):
#     numeroValido()