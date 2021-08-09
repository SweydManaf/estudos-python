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
# Arquivo: listagem\capitulo 08\08.12 - Função modificada para facilitar o rastreamento.py
##############################################################################

def fatorial(n):
     print("Calculando o fatorial de %d" % n)
     if n==0 or n == 1:
         print("Fatorial de %d = 1" % n)
         return 1
     else:
         fat = n * fatorial(n-1)
         print(" fatorial de %d = %d" % (n, fat) )
     return fat
fatorial(4)
