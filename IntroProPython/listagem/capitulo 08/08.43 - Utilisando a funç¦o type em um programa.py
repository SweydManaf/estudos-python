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
# Arquivo: listagem\capitulo 08\08.43 - Utilisando a função type em um programa.py
##############################################################################

import types
def diz_o_tipo(a):
    tipo = type(a)
    if tipo == str:
        return("String")
    elif tipo == list:
        return("Lista")
    elif tipo == dict:
        return("Dicionário")
    elif tipo == int:
        return("Número inteiro")
    elif tipo == float:
        return("Número decimal")
    elif tipo == types.FunctionType:
        return("Função")
    elif tipo == types.BuiltinFunctionType:
        return("Função interna")
    else:
        return(str(tipo))

print(diz_o_tipo(10))
print(diz_o_tipo(10.5))
print(diz_o_tipo("Alô"))
print(diz_o_tipo([1,2,3]))
print(diz_o_tipo({"a":1, "b":50}))
print(diz_o_tipo(print))
print(diz_o_tipo(None))



