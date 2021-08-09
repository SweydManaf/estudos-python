import os
import sys

if len(sys.argv) != 2:
    print('Uso ex09-32.py nome')
else:
    nome = str(sys.argv[1])
    if os.path.isdir(nome):
        print('E e um diretorio.')
    elif os.path.isfile(nome):
        print('Mas nao e um diretorio e sim um arquivo. ')
    else:
        print(f'O diretorio {nome} nao existe')