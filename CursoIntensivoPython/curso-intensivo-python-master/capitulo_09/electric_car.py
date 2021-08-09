"""Um conjunto de classes que pode ser usado para representar carros elétricos."""

from capitulo_09.car import Car


class Battery:
    """Uma tentativa simples de modelar uma bateria para um imagem elétrico."""

    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        """
        Exibe uma frase sobre a distância que o imagem é capaz de
        percorrer com essa bateria.
        """
        global range
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        print(f'This car go approximately {range} miles on a full charge.')


class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai. Em seguida, inicializa
        os atributos específicos de um imagem elétrico.
        """
        super().__init__(make, model, year)
        # Atributos de ElectricCar.
        self.battery = Battery()

    def fill_gas_tank(self, gas):
        """Carros elétricos não têm tanques de gasolina."""
        print("This car doesn't need a gas tank!")
