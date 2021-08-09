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
# Arquivo: exercicios\capitulo 08\exercicio-08-08.py
##############################################################################

def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a,b):
    return abs(a*b) / mdc(a,b)

print("MMC 10 e 5 --> %d" % mmc(10,5))
print("MMC 32 e 24 --> %d" % mmc(32,24))
print("MMC 5 e 3 --> %d" % mmc(5,3))

