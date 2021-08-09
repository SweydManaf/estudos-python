class Usuario:
    """Essa classe tenta representar um simples perfil de usuário."""

    def __init__(
            self, p_nome: str, u_nome: str, nome_de_usuario: str,
            email: str, localidade: str, idade: int, sexo: str):
        """
        -> Inicializa os atributos da classe contendo
        informações sobre o usuário.
        :param p_nome: Primeiro nome do usuário.
        :param u_nome: Último nome do usuário.
        :param nome_de_usuario: Nome de usuário.
        :param email: E-mail do usuário.
        :param localidade: Lugar em que o usuário vive.
        :param idade: Idade do usuário.
        :param sexo: Sexo do usuário, M ou F.
        """
        self.p_nome = p_nome.title()
        self.u_nome = u_nome.title()
        self.nome_de_usuario = nome_de_usuario
        self.email = email
        self.localidade = localidade.title()
        self.idade = idade
        self.sexo = sexo.upper()
        # Nome completo
        self.nome_completo = f'{self.p_nome} {self.u_nome}'

    def descrever_usuario(self) -> None:
        """Mostra um resumo das informações do usuário."""
        print(f'\nNome de usuário: {self.nome_de_usuario}'
              f'\n\tNome completo: {self.nome_completo}'
              f'\n\tE-mail: {self.email}'
              f'\n\tLocalidade: {self.localidade}' 
              f'\n\tIdade: {self.idade}'
              f'\n\tSexo: {self.sexo}')

    def saudar_usuario(self) -> None:
        """Mostra uma saudação personalizada ao usuário."""
        print(f'\nSeja bem vindo de volta, {self.nome_de_usuario}!')


usuario_1 = Usuario(
    'william', 'rodrigues', 'willy',
    'will@example.com', 'ceará', 19, 'M'
    )
usuario_1.descrever_usuario()
usuario_1.saudar_usuario()

usuario_2 = Usuario(
    'kelly', 'alves', 'kelalvs',
    'kelly@example.com', 'rio de janeiro', 20, 'F'
    )
usuario_2.descrever_usuario()
usuario_2.saudar_usuario()

usuario_3 = Usuario(
    'iago', 'viana', 'iabo',
    'iago@example.com', 'rio de janeiro', 27, 'M'
    )
usuario_3.descrever_usuario()
usuario_3.saudar_usuario()

usuario_4 = Usuario(
    'igor', 'martins', 'igu',
    'igor@example.com', 'são paulo', 20, 'M'
    )
usuario_4.descrever_usuario()
usuario_4.saudar_usuario()

usuario_5 = Usuario(
    'bruno', 'souza', 'brusou',
    'bruno@example.com', 'paraíba', 21, 'M'
    )
usuario_5.descrever_usuario()
usuario_5.saudar_usuario()
