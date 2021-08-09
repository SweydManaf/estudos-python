billy = {
    'tipo': 'papagaio',
    'dono': 'joão',
    }
lessie = {
    'tipo': 'cachorro',
    'dono': 'william',
    }
bela = {
    'tipo': 'gato',
    'dono': 'kelly',
    }
john = {
    'tipo': 'coelho',
    'dono': 'gabriela',
    }
luke = {
    'tipo': 'gato',
    'dono': 'bia',
    }

pets = [billy, lessie, bela, john, luke]
for i, pet in enumerate(pets):
    print(f'Tipo do {i + 1}° pet: {pet["tipo"].title()}\n'
          f'Dono do {i + 1}° pet: {pet["dono"].title()}\n')
