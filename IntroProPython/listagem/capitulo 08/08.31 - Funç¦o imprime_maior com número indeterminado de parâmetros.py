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
# Arquivo: listagem\capitulo 08\08.31 - Função imprime_maior com número indeterminado de parâmetros.py
##############################################################################

def imprime_maior(mensagem, *numeros):
     maior = None
     for e in numeros:
         if maior == None or maior < e:
               maior = e
     print(mensagem, maior)
imprime_maior("Maior:",5,4,3,1)
imprime_maior("Max:", *[1,7,9])
