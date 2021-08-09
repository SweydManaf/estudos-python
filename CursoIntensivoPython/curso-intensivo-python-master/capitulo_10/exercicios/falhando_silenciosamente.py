import modulo_arquivos as ma

arquivos = ['arquivos_de_texto/gatos.txt',
            'arquivos_de_texto/cachorros']

for i, arquivo in enumerate(arquivos):
    linhas = ma.ler_arquivo(arquivo)
    if i == 0:
        print('Nomes dos gatos:')
    else:
        print('\nNomes dos cachorros:')
    if linhas:
        for linha in linhas:
            print(linha.rstrip())
