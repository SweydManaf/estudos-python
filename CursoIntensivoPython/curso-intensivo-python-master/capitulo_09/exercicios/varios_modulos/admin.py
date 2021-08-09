from usuario import Usuario


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
