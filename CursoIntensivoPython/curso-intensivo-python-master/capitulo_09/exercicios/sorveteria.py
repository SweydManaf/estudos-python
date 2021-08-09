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
        # Número de pessoas servidas no dia.
        self.pessoas_atendidas = 0

    def descrever_restaurante(self) -> None:
        """Descreve as informações do restaurante."""
        print(f'Nome do restaurante: {self.nome}'
              f'\nTipo de cozinha: {self.tipo}')

    def restaurante_aberto(self) -> None:
        """Exibe uma mensagem mostrando que o restaurante está aberto."""
        print(f'\nO restaurante {self.nome} está aberto!')

    def restaurante_fechado(self) -> None:
        """Exibe uma mensagem mostrando que o restaurante fechou."""
        print(f'\nO restaurante {self.nome} fechou por hoje!')

    def mostrar_pessoas_atendidas(self) -> None:
        """
        -> Exibe uma frase mostrando quantas pessoas foram atendidas
        pelo restaurante naquele dia.
        """
        print(f'O restaurante atendeu {self.pessoas_atendidas} pessoas hoje.')

    def definir_pessoas_atendidas(self, pessoas_atendidas) -> None:
        """Define a quantidade de pessoas atendidas pelo restaurante."""
        self.pessoas_atendidas = pessoas_atendidas

    def atualizar_pessoas_atendidas(self, pessoas_atendidas) -> None:
        """Incrementa mais pessoas atendidas em um dia de funcionamento."""
        self.pessoas_atendidas += pessoas_atendidas


class Sorveteria(Restaurante):
    """
    -> Essa classe herda as características de um restaurante para
    tentar representar uma sorveteria.
    """

    def __init__(self, nome_do_restaurante: str):
        """
        -> Inicializa os atributos da classe-pai. Depois inicializa
        os atributos específicos de uma sorveteria.
        """
        super().__init__(nome_do_restaurante, tipo_de_cozinha='Sorveteria')
        # Atributos de Sorveteria.
        self.sabores = ['morango', 'flocos', 'chocolate', 'creme', 'baunilha']

    def mostrar_sabores(self) -> None:
        """Exibe os sabores disponíveis da sorveteria."""
        print(f'\nSabores disponíveis na sorveteria {self.nome}:')
        for sabor in self.sabores:
            print(f'\t{sabor.title()}')


sorveteria = Sorveteria('bom gosto')
sorveteria.descrever_restaurante()
sorveteria.restaurante_aberto()
sorveteria.mostrar_sabores()
