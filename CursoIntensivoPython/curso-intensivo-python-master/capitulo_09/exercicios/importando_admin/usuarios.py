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
        # Nome completo.
        self.nome_completo = f'{self.p_nome} {self.u_nome}'
        # Tentativas de login.
        self.tentativas_de_login = 0

    def descrever_usuario(self) -> None:
        """Mostra um resumo das informações do usuário."""
        print(f'Nome de usuário: {self.nome_de_usuario}'
              f'\n\tNome completo: {self.nome_completo}'
              f'\n\tE-mail: {self.email}'
              f'\n\tLocalidade: {self.localidade}' 
              f'\n\tIdade: {self.idade}'
              f'\n\tSexo: {self.sexo}')

    def saudar_usuario(self) -> None:
        """Mostra uma saudação personalizada ao usuário."""
        print(f'\nSeja bem vindo de volta, {self.nome_de_usuario}!')

    def atualizar_tentativas_de_login(self) -> None:
        """Incrementa em 1 as tentativas de login de um usuário."""
        self.tentativas_de_login += 1

    def resetar_tentativas_de_login(self) -> None:
        """Reseta para 0 as tentativas de login de um usuário."""
        self.tentativas_de_login = 0


class Privilegios:
    """
    -> Uma tentativa simples de criar e mostrar os privilégios que
    um usuário Admin possui.
    """

    def __init__(self):
        """Inicializa os atributos dos privilégios de um usuário Admin."""
        self.privilegios = [
            'pode adicionar um post',
            'pode deletar um post',
            'pode banir um usuário',
            'pode modificar um post',
            'pode acessar as informações dos usuários',
            'pode desbanir um usuário',
            'pode verificar as tentativas de login',
            'pode ver quem está logado',
            'pode resetar as tentativas de login',
            ]

    def mostrar_privilegios(self) -> None:
        """Exibe os privilégios de um usuário Admin."""
        print(f'\nPrivilégios do Admin:')
        for privilegio in sorted(self.privilegios):
            print(f'\t- {privilegio.capitalize()}.')


class Admin(Usuario):
    """
    -> Essa classe herda as características de um usuário normal
    para tentar representar um usuário Admin.
    """

    def __init__(
            self, p_nome: str, u_nome: str, nome_de_usuario: str,
            email: str, localidade: str, idade: int, sexo: str):
        """
        -> Inicializa os atributos da classe-pai, logo em seguida
        inicializa os atributos específicos de um usuário Admin.
        """
        super().__init__(
            p_nome, u_nome, nome_de_usuario,
            email, localidade, idade, sexo)
        # Atributos de Admin.
        self.privilegios = Privilegios()
