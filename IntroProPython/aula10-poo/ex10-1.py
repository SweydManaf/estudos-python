class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 32
        self.marca = 'LG'

tv = Televisao()
print(f'On:{tv.ligada}'
      f'\nChannel:{tv.canal}'
      f'\nSize:{tv.tamanho}'
      f'\nMarca:{tv.marca}')
