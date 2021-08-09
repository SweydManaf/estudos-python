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
# Arquivo: listagem\capitulo 09\09.08 - Criação de uma pagina inicial em Python.py
##############################################################################

pagina = open("pagina.html","w", encoding = "utf-8")
pagina.write("<!DOCTYPE html>\n")
pagina.write("<html lang=\"pt-BR\">\n")
pagina.write("<head>\n")
pagina.write("<meta charset=\"utf-8\">\n")
pagina.write("<title>Título da Página</title>\n")
pagina.write("</head>\n")
pagina.write("<body>\n")
pagina.write("Olá!")
for l in range(10):
     pagina.write("<p>%d</p>\n" % l)
pagina.write("</body>\n")
pagina.write("</html>\n")
pagina.close()
