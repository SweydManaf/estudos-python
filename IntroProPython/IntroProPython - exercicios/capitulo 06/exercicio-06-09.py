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
# Arquivo: exercicios\capitulo 06\exercicio-06-09.py
##############################################################################

L = [15,7,27,39]
p = int(input("Digite o valor a procurar (p):"))
v = int(input("Digite o outro valor a procurar (v):"))
x = 0
achouP = False
achouV = False
primeiro = 0
while x < len(L):
     if L[x] == p:
         achouP = True
         if not achouV:
            primeiro = 1
     if L[x] == v:
         achouV = True
         if not achouP:
            primeiro = 2
     x += 1
if achouP:
     print("p: %d encontrado" % p)
else:
     print("p: %d não encontrado" % p)
if achouV:
     print("v: %d encontrado" % v)
else:
     print("v: %d não encontrado" % v)
if primeiro == 1:
    print("p foi achado antes de v")
elif primeiro == 2:
    print("v foi achado antes de p")

