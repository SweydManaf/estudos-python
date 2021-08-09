pizzas = ['calabresa', 'portuguesa', 'frango']
amigo_pizzas = pizzas[:]
pizzas.append('americana')
amigo_pizzas.append('napolitana')

print('Minhas pizzas favoritas são:')
for pizza in pizzas:
    print(f'\t{pizza.title()}')

print('\nAs pizzas favoritas de meu amigo são:')
for pizza in amigo_pizzas:
    print(f'\t{pizza.title()}')
