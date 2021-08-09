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
# Arquivo: listagem\capitulo 09\09.26 - Árvore de diretorios sendo percorrida.py
##############################################################################

import os
import sys
for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
     print("\nCaminho:", raiz)
     for d in diretorios:
         print("   %s/" % d)
     for f in arquivos:
         print("   %s" % f)
     print("%d diretório(s), %d arquivo(s)" % (len(diretorios), len(arquivos)))
