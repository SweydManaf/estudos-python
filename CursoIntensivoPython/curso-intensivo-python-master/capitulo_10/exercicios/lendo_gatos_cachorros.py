import modulo_arquivos as ma

arquivos = ['arquivos_de_texto/gatos.txt',
            'arquivos_de_text/cachorros.txt']

for i, arquivo in enumerate(arquivos):
    if i == 0:
        print('Nomes dos gatos:')
    else:
        print('\nNomes dos cachorros:')
    ma.mostrar_arquivo(arquivo, 3)
