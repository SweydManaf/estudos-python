import modulo_arquivos as ma

arquivo = 'arquivos_de_texto/aprendendo_python.txt'

while True:
    print('\nEm Python podemos...?\n'
          f"Digite 'sair' para parar o programa.\n")
    mensagem = str(input('Responda: ')).lower().strip()

    if mensagem == 'sair':
        modo = int(input('\nDigite o número do modo que o arquivo será lido: '))
        ma.mostrar_arquivo(arquivo, modo)
        break
    else:
        ma.escrever_mensagem(arquivo, mensagem)
