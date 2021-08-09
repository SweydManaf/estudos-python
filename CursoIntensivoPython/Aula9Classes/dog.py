class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'O {self.name} agora esta sentado.')

    def roll_over(self):
        print(f'O {self.name} esta rolando!')

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print(f'O nome do meu cachro e {my_dog.name.title()}')
print(f'O meu cachoro tem {str(my_dog.age)} anos de idade.')
my_dog.sit()

print(f'\nO nome do seu cachoro e {your_dog.name.title()}')
print(f'O seu cachoro tem {str(your_dog.age)} anos de idade')
your_dog.sit()

