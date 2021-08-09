"""Uma classe que pode ser usada para representar um imagem."""


class Car:
    """Uma tentativa simples de representar um imagem."""

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um imagem."""
        self.make = make
        self.model = model
        self.year = year
        # Esse atributo não precisa de um parâmetro.
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = f'{self.year} {self.make} {self.model}'

        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do imagem."""
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """
        Define o valor de leitura do hodômetro com o valor especificado.
        Rejeita a alteração se for tentativa de definir um valor menor
        para o hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self, gas):
        """Enche o tanque de gasolina do imagem com o valor especificado."""
        self.gas_tank += gas
