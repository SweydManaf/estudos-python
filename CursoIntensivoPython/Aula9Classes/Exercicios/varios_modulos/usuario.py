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

