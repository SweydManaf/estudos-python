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
# Arquivo: exercicios\capitulo 06\exercicio-06-05.py
##############################################################################

último = 10
fila = list(range(1,último+1))
while True:
     print("\nExistem %d clientes na fila" % len(fila))
     print("Fila atual:", fila)
     print("Digite F para adicionar um cliente ao fim da fila,")
     print("ou A para realizar o atendimento. S para sair.")
     operação = input("Operação (F, A ou S):")
     x=0
     sair = False
     while x < len(operação):
         if operação[x] == "A":
             if(len(fila))>0:
                   atendido = fila.pop(0)
                   print("Cliente %d atendido" % atendido)
             else:
                   print("Fila vazia! Ninguém para atender.")
         elif operação[x] == "F":
             último += 1 # Incrementa o ticket do novo cliente
             fila.append(último)
         elif operação[x] == "S":
             sair = True
             break
         else:
             print("Operação inválida: %s na posição %d! Digite apenas F, A ou S!" % (operação[x],x))
         x = x + 1
     if(sair):
        break
