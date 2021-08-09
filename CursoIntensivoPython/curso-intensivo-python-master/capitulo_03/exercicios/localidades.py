locais = ['Torre Eiffel',
          'Machu Pichu',
          'Cristo Redentor',
          'Coliseu',
          'Muralha da China']

print(f'Aqui está a lista original:\n{locais}')
print(f'\nAqui está a lista ordenada:\n{sorted(locais)}')
print(f'\nAqui está a lista original novamente:\n{locais}')
print(f'\nAqui está a lista ordenada inversamente:\n{sorted(locais, reverse=True)}')
print(f'\nAqui está a lista original novamente:\n{locais}')

locais.reverse()
print(f'\nAqui está a lista com a ordem invertida:\n{locais}')
locais.reverse()
print(f'\nAqui está a lista com a ordem original:\n{locais}')

locais.sort()
print(f'\nAqui está a lista ordenada:\n{locais}')
locais.sort(reverse=True)
print(f'\nAqui está a lista ordenada inversamente:\n{locais}')
