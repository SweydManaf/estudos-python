rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'mississippi': 'estados unidos',
}

for rio, pais in rios.items():
    print(f'O {rio.title()} corre pelo {pais.title()}.')

print('\nRios:')
for rio in rios.keys():
    print(f'\t{rio.title()}')

print('\nPaíses:')
for pais in rios.values():
    print(f'\t{pais.title()}')
