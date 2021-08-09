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
# Arquivo: exercicios\capitulo 05\exercicio-05-25.py
##############################################################################

# Atenção: na primeira edição do livro, a fórmula foi publicada errada.
# A fórmula correta é p = ( b + ( n / b ) ) / 2
# A função abs foi utilizada para calcular o valor absoluto de um número,
# ou seja, seu valor sem sinal.
# Exemplos: abs(1) retorna 1 e abs(-1) retorna 1

n=float(input("Digite um número para encontrar a sua raiz quadrada: "))
b=2
while abs(n-(b*b))>0.00001:
    p=(b+(n/b))/2
    b=p
print ("A raiz quadrada de %d é aproximadamente %8.4f" % (n, p))

