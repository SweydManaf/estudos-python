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
# Arquivo: exercicios\capitulo 09\exercicio-09-20.py
##############################################################################

agenda = []

def pede_nome():
     return(input("Nome: "))

def pede_telefone():
     return(input("Telefone: "))

def mostra_dados(nome, telefone):
     print("Nome: %s Telefone: %s" % (nome, telefone))

def pede_nome_arquivo():
     return(input("Nome do arquivo: "))

def pesquisa(nome):
     mnome = nome.lower()
     for p, e in enumerate(agenda):
         if e[0].lower() == mnome:
               return p
     return None

def novo():
     global agenda
     nome = pede_nome()
     telefone = pede_telefone()
     agenda.append([nome, telefone])

def apaga():
     global agenda
     nome = pede_nome()
     p = pesquisa(nome)
     if p != None:
         del agenda[p]
     else:
         print("Nome não encontrado.")

def altera():
     p = pesquisa(pede_nome())
     if p != None:
         nome = agenda[p][0]
         telefone = agenda[p][1]
         print("Encontrado:")
         mostra_dados(nome, telefone)
         nome = pede_nome()
         telefone = pede_telefone()
         agenda[p] = [nome, telefone]
     else:
         print("Nome não encontrado.")

def lista():
     print("\nAgenda\n\n------")
     # Usamos a função enumerate para obter a posição na agenda
     for posição, e in enumerate(agenda):
         # Imprimimos a posição, sem saltar linha
         print("Posição: %d " % posição, end="")
         mostra_dados(e[0], e[1])
     print("------\n")

def lê():
     global agenda
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "r", encoding = "utf-8")
     agenda = []
     for l in arquivo.readlines():
         nome, telefone = l.strip().split("#")
         agenda.append([nome, telefone])
     arquivo.close()

def ordena():
    # Você pode ordenar a lista como mostrado no livro
    # com o método de bolhas (bubble sort)
    # Ou combinar o método sort do Python com lambdas para
    # definir a chave da lista
    # agenda.sort(key=lambda e: return e[0])
    fim = len(agenda)
    while fim > 1:
        i=0
        trocou = False
        while i < (fim - 1):
            if agenda[i]>agenda[i + 1]:
                # Opção: agenda[i], agenda[i+1] = agenda[i+1], agenda[i]
                temp = agenda[i + 1]
                agenda[i + 1] = agenda[i]
                agenda[i] = temp
                trocou = True
            i+=1
        if not trocou:
             break

def grava():
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "w", encoding = "utf-8")
     for e in agenda:
         arquivo.write("%s#%s\n" % (e[0], e[1]))
     arquivo.close()

def valida_faixa_inteiro(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
     print("""
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista
   5 - Grava
   6 - Lê
   7 - Ordena por nome

   0 - Sai
""")
     print("\nNomes na agenda: %d\n" % len(agenda))
     return valida_faixa_inteiro("Escolha uma opção: ",0,7)

while True:
     opção = menu()
     if opção == 0:
         break
     elif opção == 1:
         novo()
     elif opção == 2:
         altera()
     elif opção == 3:
         apaga()
     elif opção == 4:
         lista()
     elif opção == 5:
         grava()
     elif opção == 6:
         lê()
     elif opção == 7:
         ordena()
