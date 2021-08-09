##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2017
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/2012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Primeira reimpressão - Segunda edição - Maio/2015
# Segunda reimpressão - Segunda edição - Janeiro/2016
# Terceira reimpressão - Segunda edição - Junho/2016
# Quarta reimpressão - Segunda edição - Março/2017
#
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem\capitulo 04\04.06 - Conta de Telefone com três faixas de preço.py
##############################################################################

minutos = int(input("Quantos minutos você utilizou este mês:"))
if minutos < 200:
     preço = 0.20
else:
     if minutos < 400:
         preço = 0.18
     else:
         preço = 0.15
print("Você vai pagar este mês: R$%6.2f" % (minutos * preço))
