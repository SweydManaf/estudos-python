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
# Arquivo: listagem\capitulo 09\09.23 - Obtenção de data e hora por nome.py
##############################################################################

import time
agora = time.localtime()
print("Ano: %d" % agora.tm_year)
print("Mês: %d" % agora.tm_mon)
print("Dia: %d" % agora.tm_mday)
print("Hora: %d" % agora.tm_hour)
print("Minuto: %d" % agora.tm_min)
print("Segundo: %d" % agora.tm_sec)
print("Dia da semana: %d" % agora.tm_wday)
print("Dia no ano: %d" % agora.tm_yday)
print("Horário de verão: %d" % agora.tm_isdst)
