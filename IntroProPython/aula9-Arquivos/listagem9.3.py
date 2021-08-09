import sys

print(f'Numero de parametros : {len(sys.argv)}')
for n, p in enumerate(sys.argv):
    print(f'Parametro {n} = {p}')