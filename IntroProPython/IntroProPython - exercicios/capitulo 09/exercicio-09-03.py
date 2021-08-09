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
# Arquivo: exercicios\capitulo 09\exercicio-09-03.py
##############################################################################

# Assume que pares e ímpares contém apenas números inteiros
# Assume que os valores em cada arquivo estão ordenados
# Os valores não precisam ser sequenciais
# Tolera linhas em branco
# Pares e ímpares podem ter número de linhas diferentes

def lê_número(arquivo):
    while True:
        número = arquivo.readline()
        # Verifica se conseguiu ler algo
        if número == "":
            return None
        # Ignora linhas em branco
        if número.strip()!= "":
            return int(número)

def escreve_número(arquivo,n):
    arquivo.write("%d\n" % n)


pares = open("pares.txt","r")
ímpares = open("ímpares.txt","r")
pares_ímpares = open("pareseimpares.txt","w")
npar = lê_número(pares)
nímpar = lê_número(ímpares)
while True:
    if npar == None and nímpar == None: # Termina se ambos forem None
        break
    if npar != None and (nímpar==None or npar<=nímpar):
        escreve_número(pares_ímpares, npar)
        npar = lê_número(pares)
    if nímpar != None and (npar==None or nímpar<=npar):
        escreve_número(pares_ímpares, nímpar)
        nímpar = lê_número(ímpares)

pares_ímpares.close()
pares.close()
ímpares.close()

