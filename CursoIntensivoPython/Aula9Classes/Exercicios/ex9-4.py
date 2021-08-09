class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Nome do restaurante: {self.name.capitalize()}')
        print(f'Tipo de cozinha: {self.type.capitalize()} ')

    def open_restaurant(self):
        print(f'\nO restaurante {self.name} esta aberto.')

    def close_restaurant(self):
        print(f'O restaurante {self.name} fechou por hoje!')

    def show_serveds(self):
        print(f'O restaurante atendeu {self.number_served} pessoas')

    def set_number_served(self, number_served):
        self.number_served = number_served


    def increment_number_served(self, served):
        if served >= 0:
            self.number_served += served
        else:
            print("\nYou can't roll down servers.")

restaurant = Restaurant('TAVERNA', 'DOCES')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print('\nUma hora depois...')
restaurant.set_number_served(8)
print(f'Pessoas atendidas ate o momento: {restaurant.number_served}')

print('\nDepois de 8 horas...')
restaurant.increment_number_served(18)
print(f'Pessoas atendidas ate o momento: {restaurant.number_served}')
restaurant.close_restaurant()
print('\nFinal do expediente...')
restaurant.increment_number_served(6)
restaurant.show_serveds()
