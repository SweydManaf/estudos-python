class Pizza:
    pedacos = 8

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

    @staticmethod
    def ingredientes():
        return 'Ingredientes'

class Mussarela(Pizza):

    @staticmethod
    def ingredientes():
        return ['queijo',
                'molho de tomate',
                'oregano',
                'azeitona']