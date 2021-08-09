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
# Arquivo: exercicios\capitulo 09\exercicio-09-18.py
##############################################################################

# Se o # aparecer no nome ou telefone de uma entrada na agenda,
# ocorrerá um erro ao ler o arquivo.
# Este erro ocorre pois o número de campos esperados na linha será diferente
# de 2 (nome e telefone).
# O programa não tem como saber que o caracter faz parte de um campo ou de outro.
# Uma solução para este problema é substituir o # dentro de um campo antes de salvá-lo.
# Desta forma, o separador de campos no arquivo não seria confundido com o conteúdo.
# Durante a leitura a substituição tem que ser revertida, de forma a obter o mesmo conteúdo.


