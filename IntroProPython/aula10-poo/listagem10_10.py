from IntroProPython.aula10poo.cliente import Cliente
from IntroProPython.aula10poo.banco import Banco
from IntroProPython.aula10poo.conta import Conta

joao = Cliente('Joao da Silva', '3241-599')
maria = Cliente('Maria Silva', '7231-9955')
jose = Cliente('Jose Vargas', '9721-3040')
contaJM = Conta([jose, maria], 100, 50)
contaJ = Conta([jose], 10, 20)
tatu = Banco('Tatu')
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_conta()