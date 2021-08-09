lugares_favoritos = {
    'william': ['casa', 'casa da vó', 'rio de janeiro'],
    'bill': ['casa', 'escola'],
    'jen': ['casa', 'escola', 'rio de janeiro'],
    }

for nome, lugares in lugares_favoritos.items():
    if len(lugares) != 1:
        print(f'\nOs lugares favorito de {nome.title()} são:')
        for lugar in lugares:
            print(f'\t{lugar.title()}')
    else:
        print(f'\nO lugar favorito de {nome.title()} é {lugares[0].title()}.')
