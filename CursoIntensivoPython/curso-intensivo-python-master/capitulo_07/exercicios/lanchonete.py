# Começa com uma lista de sanduíches que foram pedidos,
# e uma lista vazia dos sanduíches que forem ficando prontos.
sanduiches_pedidos = [
    'bauru', 'vada pav', 'roti john',
    'bánh mì', 'katsu-sando', 'BLT',
    'cemita', 'croque madame', 'falafel',
    'fischbrötchen', 'chacarero',
    ]
sanduiches_prontos = list()

# Prepara cada sanduíche até que não haja mais sanduíches pedidos.
# Transfere cada sanduíche preparado para a lista de sanduíches prontos.
while sanduiches_pedidos:
    sanduiche_atual = sanduiches_pedidos.pop()
    print(f'Sanduíche {sanduiche_atual.title()} preparado.'
          if sanduiche_atual != 'BLT' else
          f'Sanduíche {sanduiche_atual.upper()} preparado.')
    sanduiches_prontos.append(sanduiche_atual)

# Exibe todos os sanduíches prontos.
print('\nOs seguintes sanduíches ficaram prontos:')
for sanduiche_pronto in sanduiches_prontos:
    print(f'\t{sanduiche_pronto.title()}'
          if sanduiche_pronto != 'BLT' else
          f'\t{sanduiche_pronto.upper()}')
