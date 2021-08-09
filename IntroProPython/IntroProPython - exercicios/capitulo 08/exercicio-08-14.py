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
# Arquivo: exercicios\capitulo 08\exercicio-08-14.py
##############################################################################

import random

palavras = [
          "casa",
          "bola",
          "mangueira",
          "uva",
          "quiabo",
          "computador",
          "cobra",
          "lentilha",
          "arroz"
     ]
# Escolhe uma palavra aleatoriamente
palavra = palavras[random.randint(0,len(palavras)-1)]

digitadas = []
acertos = []
erros = 0

linhas_txt = """
X==:==
X  :
X
X
X
X
=======

"""

linhas = []

for linha in linhas_txt.splitlines():
     linhas.append(list(linha))

while True:
     senha = ""
     for letra in palavra:
         senha += letra if letra in acertos else "."
     print(senha)
     if senha == palavra:
         print("Você acertou!")
         break
     tentativa = input("\nDigite uma letra:").lower().strip()
     if tentativa in digitadas:
         print("Você já tentou esta letra!")
         continue
     else:
         digitadas += tentativa
         if tentativa in palavra:
               acertos += tentativa
         else:
               erros += 1
               print("Você errou!")
               if erros == 1:
                    linhas[3][3] = "O"
               elif erros == 2:
                    linhas[4][3] = "|"
               elif erros == 3:
                    linhas[4][2] = "\\"
               elif erros == 4:
                    linhas[4][4] = "/"
               elif erros == 5:
                    linhas[5][2] = "/"
               elif erros == 6:
                    linhas[5][4] = "\\"

     for l in linhas:
          print("".join(l))
     if erros == 6:
         print("Enforcado!")
         print("A palavra secreta era: %s" % palavra)
         break
