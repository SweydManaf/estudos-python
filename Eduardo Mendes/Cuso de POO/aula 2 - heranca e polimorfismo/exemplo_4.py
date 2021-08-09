class Pizza:
    pedacos = 8

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

class Mussarela(Pizza):
    ...

class Calabresa(Pizza):
    ...

class MeioAMeio(Mussarela, Calabresa):
    ...