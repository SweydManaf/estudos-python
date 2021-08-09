try:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
except (TypeError, ValueError):
    print('ERRO: digite apenas números inteiros.')
else:
    soma = n1 + n2
    print(f'\nA soma entre {n1} e {n2} é igual a {soma}.')
