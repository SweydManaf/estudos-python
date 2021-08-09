from IntroProPython.aula10poo.listagem10_4 import Cliente
class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.saldo = 0
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        for dado in self.clientes:
            print(f'NOME: {dado.nome}\nTELEFONE: {dado.telefone}\n')
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

joao = Cliente('Joao', '888-1234')
jose = Cliente('Jose', '1-4321')
conta = Conta([joao, jose], 554, 500)
conta.resumo()



