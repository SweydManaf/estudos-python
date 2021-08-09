#Nilo soluction

import os
import sys
import urllib.request

def gera_listagem(pagina, diretorio):
    nraiz = os.path.abspath(diretorio).count(os.sep)
    for raiz, diretorio, arquivos in os.walk(diretorio):
        nivel =raiz.count(os.sep)  - nraiz
        pagina.write(f'<p>{raiz}</p>')
        for a in arquivos:
            caminho_completo = os.path.join(raiz, a)
            tamanho = os.path.getsize(caminho_completo)
            link = urllib.request.pathname2url(caminho_completo)
            pagina.write(f'<p><a href="{link}">{a}</a> ({tamanho} bytes)</p>')


if len(sys.argv) < 2:
    print('Digite o nome do diretorio para coletar os arquivos!')
    sys.exit(1)


diretorio = sys.argv[1]

pagina = open('arquivos.html', 'w', encoding = 'utf-8')
pagina.write('''
<DOCTYPE html>
<html lang="br">
<head>
<meta charset="utf-8">
<title>Arquivos</title>
</head>
<body>
''')
pagina.write(f'Arquivos encontrados a partir do diretorio: {diretorio}')
gera_listagem(pagina, diretorio)
pagina.write('''
</body>
</html>''')
pagina.close()