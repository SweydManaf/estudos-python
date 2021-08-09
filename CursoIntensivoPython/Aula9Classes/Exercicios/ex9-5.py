# Tentativa de login
from time import sleep

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
        print(f'    Nome completo: {self.nome_completo}')
        print(f'    E-mail: {self.email}')
        print(f'    Localidade: {self.localidade}')
        print(f'    Idade: {self.idade}')
        print(f'    Sexo: {self.sexo}')

    def saudacao(self):
        print(f'Seja bem vindo, {self.nome_do_usuario}')

    def atualizar(self):
        self.tentativas += 1

    def resetar(self):
        self.tentativas = 0

def texto(msg):
    tam = int(len(msg))
    print('-='* 15)
    print(f'{msg:^30}')
    print('-=' * 15)

def pede_idade():
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('Digite uma idade valida.')
        else:
            return idade

def pede_sexo():
    while True:
        sexo = str(input('Digite sexo do usuario [M/F]: ')).upper()
        if sexo == 'M':
            return 'M'
        if sexo == 'F':
            return 'F'
        else:
            print('Digite apenas "M" ou "F" para o sexo.')


def fim():
    while True:
        sexo = str(input('Deseja continuar [S/N]: ')).upper()
        if sexo == 'S':
            return 'S'
        if sexo == 'N':
            return 'N'
        else:
            print('Digite apenas "S" ou "N".')

while True:
    texto('CADASTRE UM USUARIO')
    nome = str(input('Primeiro nome: ')).strip().title()
    apelido = str(input('Ultimo nome: ')).strip().title()
    nome_do_usuario = str(input('Defina o nome do usuario: '))
    email = str(input('Digite o E-mail: '))
    localidade = str(input('Localidade: '))
    idade = pede_idade()
    sexo = pede_sexo()
    usuario = User(nome, apelido, nome_do_usuario, email,
                   localidade, idade, sexo)

    print(f'\nTentando logar com o usario {usuario.nome_do_usuario}...')
    sleep(2)
    for t in range(0, 5):
        usuario.atualizar()
        print(f'\t{usuario.tentativas}o Tentativa...', flush=True)
        sleep(1)

    print(f'Tentativas de login: {usuario.tentativas}\n')
    sleep(2)
    usuario.saudacao()
    print('\nInformacoes do usuario: ')
    sleep(2)
    usuario.descricao_do_usuario()
    print('Resetando o numero das tentativas de login...')
    usuario.resetar()
    sleep(2)
    print(f'Tentativas de login: {usuario.tentativas}')
    sleep(3)
    if fim() == 'N':
        print('FINALIZANDO...')
        sleep(3)
        break