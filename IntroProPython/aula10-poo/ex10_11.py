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
        for o in self.clientes:
            print(f'NOME:{o.nome}\nTELEFONE:{o.telefone}')
            print(f'SALDO: {self.saldo}')
            print('='*30)


    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            return True
        return False

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPOSITO', valor])

    def extrato(self):
        print(f'Extrato CC N {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:>10} {o[1]:10.2f}')
        print(f'\n\tSaldo: {self.saldo:10.2f}')

class ContaEspecial(Conta): # 1
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo) # 2
        self.limite = limite # 3

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            return True
        return False

    def extrato(self):
        Conta.extrato(self)
        print(f'\tLimite: {self.limite}')
        print(f'\tDisponivel para saque: {self.saldo+self.limite}')

joao = Cliente('Joao', '12-311-3')
conta = ContaEspecial([joao], 3432, 50000, 10000)
conta.extrato()