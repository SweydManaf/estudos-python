from random import randint


class Dado:
    """Essa classe tenta representar um dado."""

    def __init__(self, lados: int = 6):
        """
        -> Inicializa os atributos de um dado.
        :param lados: (Padrão=6) Quantidade de lados de um dado.
        """
        self.lados = lados

    def rolar_dado(self) -> int:
        """
        -> Rola um dado entre 1 e o número de lados do dado.
        :return: Retorna o número escolhido que saiu aleatoriamente.
        """
        numero = randint(1, self.lados)

        return numero

    def rolar_dez_vezes(self) -> None:
        """
        -> Exibe a rolagem de um dado aleatoriamente dez vezes
        entre 1 e o número de lados do dado.
        """
        from time import sleep

        for rolagem in range(10):
            numero = randint(1, self.lados)
            if len(str(self.lados)) == 1:
                sleep(1)
                print(f'\tNa {rolagem + 1:2}° rolagem saiu o número {numero}')
            else:
                sleep(1)
                print(f'\tNa {rolagem + 1:2}° rolagem saiu o número {numero:2}')


dado_1 = Dado()
print('Resultados do primeiro dado:')
dado_1.rolar_dez_vezes()

dado_2 = Dado(10)
print('\nResultados do segundo dado:')
dado_2.rolar_dez_vezes()

dado_3 = Dado(20)
print('\nResultados do terceiro dado:')
dado_3.rolar_dez_vezes()
