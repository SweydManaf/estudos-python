import restaurante

restaurante = restaurante.Restaurante('stokehouse', 'buffet')
print(f'O nome do restaurante é {restaurante.nome}.')
print(f'Conhecido pelo famoso tipo de cozinha {restaurante.tipo}.\n')
restaurante.descrever_restaurante()
restaurante.restaurante_aberto()
