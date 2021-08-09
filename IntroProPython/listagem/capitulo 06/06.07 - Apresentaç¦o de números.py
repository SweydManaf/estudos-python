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
# Arquivo: listagem\capitulo 06\06.07 - Apresentação de números.py
##############################################################################

números = [0,0,0,0,0]
x = 0
while x < 5:
     números[x] = int(input("Número %d:" % (x+1)))
     x += 1
while True:
     escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
     if escolhido == 0:
         break
     print("Você escolheu o número: %d" % (números[escolhido-1]))
