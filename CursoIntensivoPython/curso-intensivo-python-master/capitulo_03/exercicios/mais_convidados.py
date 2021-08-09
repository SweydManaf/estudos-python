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

nomes.insert(0, 'Wagner Montes')
nomes.append('Mr. Catra')
nomes.insert(2, 'Isaac Newton')

for nome in nomes:
    print(f'Sir {nome}, você me concederia a honra de sua presença para um jantar?')
