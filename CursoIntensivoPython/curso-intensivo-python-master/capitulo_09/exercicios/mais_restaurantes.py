class Restaurante:
    """Essa classe tenta representar um restaurante."""

    def __init__(self, nome_do_restaurante: str, tipo_de_cozinha: str):
        """
        -> Inicializa os atributos da classe contendo
        o nome e o tipo de cozinha do restaurante.
        :param nome_do_restaurante: Nome do restaurante.
        :param tipo_de_cozinha: Tipo de cozinha do restaurante.
        """
        self.nome = nome_do_restaurante.title()
        self.tipo = tipo_de_cozinha.title()

    def descrever_restaurante(self) -> None:
        """Descreve as informações do restaurante."""
        print(f'\nNome do restaurante: {self.nome}'
              f'\nTipo de cozinha: {self.tipo}')

    def restaurante_aberto(self) -> None:
        """Exibe uma mensagem mostrando que o restaurante está aberto."""
        print(f'\nO restaurante {self.nome} está aberto!')


restaurante = Restaurante('stokehouse', 'buffet')
outro_restaurante = Restaurante('iyo', 'food truck')
ultimo_restaurante = Restaurante('gracious madre', 'jantar fino')

restaurante.descrever_restaurante()
outro_restaurante.descrever_restaurante()
ultimo_restaurante.descrever_restaurante()
