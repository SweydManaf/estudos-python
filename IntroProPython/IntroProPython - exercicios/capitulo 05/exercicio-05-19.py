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
# Arquivo: exercicios\capitulo 05\exercicio-05-19.py
##############################################################################

# Atenção: alguns valores não serão calculados corretamente
# devido a problemas com arredondamento e da representação de 0.01
# em ponto flutuante. Uma alternativa é multiplicar todos os valores
# por 100 e realizar todos os cálculos com números inteiros.

valor = float(input("Digite o valor a pagar:"))
cédulas = 0
atual = 100
apagar = valor
while True:
     if atual <= apagar:
         apagar -= atual
         cédulas += 1
     else:
         if atual >=1:
            print("%d cédula(s) de R$%d" % (cédulas, atual))
         else:
            print("%d moeda(s) de R$%5.2f" % (cédulas, atual))
         if apagar <0.01:
               break
         elif atual == 100:
            atual = 50
         elif atual == 50:
            atual = 20
         elif atual == 20:
            atual = 10
         elif atual == 10:
            atual = 5
         elif atual == 5:
            atual = 1
         elif atual == 1:
            atual = 0.50
         elif atual == 0.50:
            atual = 0.10
         elif atual == 0.10:
            atual = 0.05
         elif atual == 0.05:
            atual = 0.02
         elif atual == 0.02:
            atual = 0.01
         cédulas = 0
