class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.saldo = 0
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f'Nome: {self.clientes[0].nome}')
        print(f'NUMERO: {self.clientes[0].telefone}')
        print(f'CC N{self.numero} Saldo: {self.saldo:10.2f}')
        print('='*30)

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
        else:
            print('SALDO INSUFICIENTE')

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPOSITO', valor])

    def extrato(self):
        print(f'Extrato CC N {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:>10} {o[1]:10.2f}')
        print(f'\n   Saldo: {self.saldo:10.2f}\n')



