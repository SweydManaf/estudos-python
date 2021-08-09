from time import sleep


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


def mostrar_titulo(texto: str) -> None:
    """
    -> Mostra um título de forma elegante.
    :param texto: String para exibi como título.
    """
    print(f'\n{"=-=" * 10}\n{texto:^30}\n{"=-=" * 10}')


while True:
    mostrar_titulo('CADASTRE UM USUÁRIO')
    primeiro_nome = str(input('Primeiro nome: '))
    ultimo_nome = str(input('Último nome: '))
    nome_usuario = str(input('Defina o nome de usuário: '))
    e_mail = str(input('Digite o E-mail: '))
    local = str(input('Localidade: '))
    while True:
        try:
            i = int(input('Idade: '))
        except (ValueError, TypeError):
            print('Digite um número inteiro para a idade.\n')
        else:
            break
    while True:
        sex = str(input('Digite o sexo do usuário [M/F]: ')).upper().strip()
        if sex in 'MF' and sex != '':
            break
        print('Digite apenas "M" ou "F" para o sexo.\n')

    usuario = Usuario(
        primeiro_nome, ultimo_nome,
        nome_usuario, e_mail, local, i, sex
        )
    print(f'\nTentando logar com o usuário {usuario.nome_de_usuario}...')
    sleep(2)
    for tentativa in range(5):
        usuario.atualizar_tentativas_de_login()
        sleep(1)
        print(f'\t{tentativa + 1}° tentativa...')
    print(f'Tentativas de login: {usuario.tentativas_de_login}')
    sleep(2)
    usuario.saudar_usuario()

    print('\nInformações do usuário:')
    sleep(2)
    usuario.descrever_usuario()

    print('\nResetando o número das tentativas de login...')
    sleep(2)
    usuario.resetar_tentativas_de_login()
    print(f'Tentativas de login: {usuario.tentativas_de_login}')
    sleep(3)

    while True:
        continuar = str(input('\nDeseja continuar?\n[S/N] ')).upper().strip()
        if continuar in 'SN' and continuar != '':
            break
        print('Digite apenas "S" ou "N".')
    if continuar == 'N':
        mostrar_titulo('FINALIZANDO...')
        sleep(3)
        break
