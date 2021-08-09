class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f'O nome do restaurante e {self.name.title()}')
        print(f'O restaurante {self.name.title()} faz {self.type.lower()} ')

    def open_restaurant(self):
        print(f'O restaurante {self.name} esta aberto.')

restaurant1 = Restaurant('TAVERNA', 'SALGADOS')
restaurant2 = Restaurant('TAYRICA', 'DOCES')
restaurant3 = Restaurant('ANY CAKES', 'BOLOS')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
