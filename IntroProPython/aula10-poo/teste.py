from IntroProPython.aula10poo.cliente import Cliente
from IntroProPython.aula10poo.conta import Conta, ContaEspecial  # 1

joao = Cliente('Joao da silva', '777-1234')
maria = Cliente('Maria da silva', '555-4321')

conta1 = Conta([joao], 1, 1000)
conta2 = ContaEspecial([maria, joao], 2, 500, 1000)  # 2
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
