class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f'O nome do restaurante e {self.name}')
        print(f'O tipo do restaurante e {self.type} ')

    def open_restaurant(self):
        print(f'O restaurante {self.name} esta aberto.')

restaurant = Restaurant('TAVERNA', 'DOCES')
restaurant.describe_restaurant()
restaurant.open_restaurant()