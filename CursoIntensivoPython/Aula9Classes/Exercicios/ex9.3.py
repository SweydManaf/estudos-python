class User():

    def __init__(self, nome, apelido, year):
        self.nome = nome
        self.apelido = apelido
        self.year = year

    def descricao(self):
        print('-'*30)
        print(f'O nome e {self.nome.title()}')
        print(f'O apelido e {self.apelido.title()}')
        print(f'Nasceu no ano de {self.year}')
        print('#'*30)

    def saudacao(self):
        print(f'Ola {self.nome.title()} {self.apelido.title()}')


user1 = User('sweyd', 'Manaf', 2005)
user2 = User('adil', 'antonio', 2006)
user3 = User('huzayf', 'wahabo', 2004)


user1.saudacao()
user1.descricao()
user2.saudacao()
user2.descricao()
user3.saudacao()
user3.descricao()