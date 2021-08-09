# Começa com uma lista de sanduíches que foram pedidos,
# e uma lista vazia dos sanduíches que forem ficando prontos.
sanduiches_pedidos = [
    'bauru', 'vada pav', 'roti john',
    'bánh mì', 'katsu-sando', 'BLT',
    'cemita', 'croque madame', 'falafel',
    'fischbrötchen', 'chacarero', 'pastrami',
    'pastrami', 'pastrami', 'pastrami',
    ]
sanduiches_prontos = list()

# Exibe uma mensagem no início informando que a lanchonete está sem pastrami.
print('INFO:\n\tA lanchonete encontra-se sem PASTRAMI no momento.'
      '\n\tPedimos desculpa pelo incômodo.')

# Enquanto houver pastrami nos pedidos,
# remove eles da lista de sanduíches pedidos.
while 'pastrami' in sanduiches_pedidos:
    sanduiches_pedidos.remove('pastrami')

# Prepara cada sanduíche até que não haja mais sanduíches pedidos.
# Transfere cada sanduíche preparado para a lista de sanduíches prontos.
while sanduiches_pedidos:
    sanduiche_atual = sanduiches_pedidos.pop()
    sanduiches_prontos.append(sanduiche_atual)

# Exibe todos os sanduíches prontos para verificar
# se não existe nenhum sanduíche de pastrami.
print('\nOs seguintes sanduíches ficaram prontos:')
for sanduiche_pronto in sanduiches_prontos:
    print(f'\t{sanduiche_pronto.title()}'
          if sanduiche_pronto != 'BLT' else
          f'\t{sanduiche_pronto.upper()}')
