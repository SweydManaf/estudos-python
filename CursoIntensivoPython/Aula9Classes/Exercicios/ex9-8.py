class User():

    def __init__(self, nome, apelido, nome_do_usuario, email,
                 localidade, idade, sexo):
        self.nome = nome
        self.apelido = apelido
        self.nome_do_usuario = nome_do_usuario
        self.email = email
        self.localidade = localidade
        self.idade = idade
        self.sexo = sexo
        self.nome_completo = f'{self.nome} {self.apelido}'
        self.tentativas = 0
    def descricao_do_usuario(self):
        print(f'Nome do usuario: {self.nome_do_usuario}')
        print(f'\tNome completo: {self.nome_completo}')
        print(f'\tE-mail: {self.email}')
        print(f'\tLocalidade: {self.localidade}')
        print(f'\tIdade: {self.idade}')
        print(f'\tSexo: {self.sexo}')

    def saudacao(self):
        print(f'\nSeja bem vindo, {self.nome_do_usuario}')

class Privileges():
    def __init__(self):

        self.privilegios = ['Pode acessar informacaoes dos usarios',
                            'Pode adicionar um post',
                            'Pode banir um usuario.',
                            'Pode deletar um post.',
                            'Pode desbanir um usuario.']

    def mostra_previlegios(self):
        print('\nPrivilegios do Admin:')
        for vantagem in self.privilegios:
            print(f'\t- {vantagem}')

class Admin(User):
    def __init__(self, nome, apelido, nome_do_usuario, email,
                 localidade, idade, sexo):
        super().__init__(nome, apelido, nome_do_usuario, email,
                 localidade, idade, sexo)
        self.privilegios = Privileges()

inicia = Admin('William','Rodrigues','Admin',
                 'will@example.com','Maputo',
                 19,'M')

inicia.descricao_do_usuario()
inicia.saudacao()
inicia.privilegios.mostra_previlegios()


