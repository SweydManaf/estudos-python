from random import choice

nomes = ['Albert Einstein', 'Robin Williams', 'William Shakespeare']
for nome in nomes:
    print(f'Sir {nome}, você me concederia a honra de sua presença para um jantar?')

# Escolha um dos nomes da lista aleatoriamente.
convidado = choice(nomes)
print(f'\nInfelizmente o {convidado} não poderá comparecer.\n')

# Coloca o novo convidado 'Stan Lee' no lugar do convidado escolhido.
nomes.insert(nomes.index(convidado), 'Stan Lee')
# Remove o convidado que não comparecerá da lista.
nomes.remove(convidado)

for nome in nomes:
    print(f'Sir {nome}, você me concederia a honra de sua presença para um jantar?')

print('\nHey, encontrei uma mesa maior, vamos chamar mais convidados!\n')

# Adiciona mais 3 pessoas na lista.
nomes.insert(0, 'Wagner Montes')
nomes.append('Mr. Catra')
nomes.insert(2, 'Isaac Newton')

for nome in nomes:
    print(f'Sir {nome}, você me concederia a honra de sua presença para um jantar?')

print('\nOps, a mesa não ficou pronta, poderei só convidar duas pessoas.\n')

for i in range(len(nomes)):
    if len(nomes) != 2:
        # Escolha um nome pra ser removido.
        nome_removido = choice(nomes)
        print(f'{nome_removido} sinto muito por isso, mas não poderei convidá-lo...')
        # Remove da lista de acordo com o índice da pessoa escolhida para ser removida.
        nomes.pop(nomes.index(nome_removido))

# Mostra os 2 restantes da lista.
print(f'\nVocê ainda está convidado {nomes[0]}.\n'
      f'Você também ainda está convidado {nomes[1]}.')

# Remove eles da lista.
del nomes[0]
del nomes[0]

# Exibe a lista vazia.
print(f'\nLista vazia: {nomes}')
