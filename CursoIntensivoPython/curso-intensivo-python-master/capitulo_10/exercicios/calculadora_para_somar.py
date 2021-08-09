while True:
    try:
        n1 = int(input('\nPrimeiro número: '))
    except ValueError:
        print('ERRO: digite apenas números inteiros.')
    else:
        break
while True:
    try:
        n2 = int(input('Segundo número: '))
    except ValueError:
        print('ERRO: digite apenas números inteiros.\n')
    else:
        break

soma = n1 + n2
print(f'\nA soma entre {n1} e {n2} é igual a {soma}.')
