# Nilo soluction

import sys
import os
# este modulo ajuda com a conversao de nomes de arquivos para links
# validos em HTML
import urllib.request

if len(sys.argv) != 2:
    print('Uso ex09-33.py nome_do_diretorio_das musicas')
    sys.exit(1)

diretorio = sys.argv[1]
pagina = open('musica.html', 'w')
pagina.write('''
<!DOCTYPE html>
<html lang="br">
<head>
<meta charset="utf-8">
<title>Musicas</title>
</head>
<body>''')
pagina.write(f'Imagens encontradas no diretorio: {diretorio}')
for entrada in os.listdir(diretorio):
    nome, extensao = os.path.splitext(entrada) # divide o nome com extensao
    if extensao in ['.jpg', '.mp3']:
        caminho_completo = os.path.join(diretorio, entrada)
        link = urllib.request.pathname2url(caminho_completo)
        pagina.write(f'<p><a href="{link}">{entrada}</a></p>')
pagina.write('''
</body>
</html>
''')
pagina.close()
