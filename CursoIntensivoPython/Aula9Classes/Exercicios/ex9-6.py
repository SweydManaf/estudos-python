class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f'O nome do restaurante e {self.name}')
        print(f'O tipo do restaurante e {self.type} ')

    def open_restaurant(self):
        print(f'\nO restaurante {self.name} esta aberto.')

class IceCreamStand(Restaurant):
    def __init__(self, name):
        super().__init__(name, type='Sorvetaria')
        self.flavors = ['Morango', 'Flocos','Chocolate',
                        'Creme', 'Baunilha']

    def mostra_sabores(self):
        print(f'\nSabores disponiveis na sorvetaria {self.name}')
        for sabor in self.flavors:
            print(f'\t{sabor}')

gelados = IceCreamStand('Bom Gosto')
gelados.describe_restaurant()
gelados.open_restaurant()
gelados.mostra_sabores()
