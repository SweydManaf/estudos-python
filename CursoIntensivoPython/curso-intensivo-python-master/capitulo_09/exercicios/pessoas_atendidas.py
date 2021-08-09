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


restaurante = Restaurante('stokehouse', 'buffet')
restaurante.descrever_restaurante()
restaurante.restaurante_aberto()

print('\nUma hora depois...')
restaurante.definir_pessoas_atendidas(8)
print(f'Pessoas atendidas até o momento: {restaurante.pessoas_atendidas}')

print('\nDepois de 8 horas...')
restaurante.atualizar_pessoas_atendidas(18)
print(f'Pessoas atendias até o momento: {restaurante.pessoas_atendidas}')
restaurante.restaurante_fechado()
print('\nFinal do expediente...')
restaurante.atualizar_pessoas_atendidas(6)
restaurante.mostrar_pessoas_atendidas()
