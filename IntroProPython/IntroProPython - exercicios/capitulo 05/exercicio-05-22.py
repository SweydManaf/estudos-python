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
# Arquivo: exercicios\capitulo 05\exercicio-05-22.py
##############################################################################

while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    opção =int(input("Escolha uma opção:"))
    if opção == 5:
        break
    elif opção >=1 and opção <5:
        n = int(input("Tabuada de:"))
        x = 1
        while x<=10:
            if opção == 1:
                print("%d + %d = %d" % (n, x, n + x))
            elif opção == 2:
                print("%d - %d = %d" % (n, x, n - x))
            elif opção == 3:
                print("%d / %d = %5.4f" % (n, x, n / x))
            elif opção == 4:
                print("%d x %d = %d" % (n, x, n * x))
            x=x+1
    else:
        print("Opção inválida!")
