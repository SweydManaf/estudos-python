class Car():
    '''Uma tentativa simples de representar um imagem.'''

    def __init__(self, make, model, year):
        '''Inicializa os atributos que descrvem um imagem.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '''Devolve um nome descritivo, formatado de modo elegante.'''
        long_name = str(f'{self.year} {self.make} {self.model}')
        return long_name.title()

    def read_odometer(self):
        '''Exibe uma frase que mostra a milhagem do imagem.'''
        print(f'This car has {str(self.odometer_reading)} miles on it.')

    def update_odometer(self, mileage):
        '''Define o valor de leitura do hodometro com o valor
        especificado.
        Rejeita a alteracao se for tentativa de definir um valor menor
        para o hodometro
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        '''Soma a quantidade especificada ao valor de leitura do
        hodometro.'''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


class Battery():
    '''Uma tentativa simples de modelar uma bateria para um imagem
    eletrico.'''

    def __init__(self, batter_size=70):
        '''Inicializa os atributos da bateria.'''
        self.battery_size = batter_size

    def describe_battery(self):
        '''Exibe uma frase que descreve a capacidade da bateria.'''
        print(f'This car has a {str(self.battery_size)}-kWh battery.')

    def get_range(self):
        '''Exibe uma frase sobre a distancia que o imagem e capaz
        de percorrer com essa bateria.'''

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f'This car can go approximately {str(range)}'
        message += ' miles on full charge.'
        print(message)


class EletricCar(Car):
    '''Representa aspectos especificos de veiculos eletricos.'''

    def __init__(self, make, model, year):
        '''Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos especificos de um imagem
        eletrico.'''
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = EletricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
