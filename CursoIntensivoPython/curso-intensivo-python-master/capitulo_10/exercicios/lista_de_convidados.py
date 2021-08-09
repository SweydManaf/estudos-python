from time import sleep

import modulo_arquivos as ma

arquivo = 'arquivos_de_texto/lista_de_convidados.txt'

# Lista que armazenará os convidados que já estão na lista de convidados.
convidados = []

while True:
    prompt = '\nSeja bem-vindo! Adicione aqui o nome do convidado na lista!'
    prompt += "\n\t(Digite 'sair' para interromper o programa.)"
    while True:
        convidado = str(input(f'{prompt}\nConvidado: ')).strip().title()
        if convidado.replace(' ', '').isalpha() and convidado != '':
            break
        print('Por favor, digite o seu nome novamente.\n')

    if convidado.lower() == 'sair':
        print('\nFinalizando o programa...')
        break

    # Lista de linhas do arquivo.
    linhas = ma.ler_arquivo(arquivo)
    if linhas:
        for linha in linhas:
            convidados.append(linha[24:].rstrip())
    else:
        print(f"\nDesculpe, o arquivo '{arquivo}' não existe.")
        continue

    if convidado in convidados:
        print(f'\nO nome {convidado} já está na lista de convidados.')
    else:
        ma.escrever_nome_dos_convidados(arquivo, convidado)
        print(f'\nOlá {convidado.title()}, seu nome '
              'foi adicionado com sucesso!')

    while True:
        prompt = '\nVocê gostaria de verificar a lista de convidados?'
        verificar_lista = str(input(f'{prompt}\n[S/N] ')).strip().upper()

        if verificar_lista in 'SN':
            if verificar_lista == 'S':
                print('\nLista de convidados:')

                # Lista de linhas do arquivo.
                linhas = ma.ler_arquivo(arquivo)
                for linha in linhas:
                    sleep(0.5)
                    print(f'\t{linha.rstrip()}')
                sleep(3)
            else:
                print('\nTudo bem, retomando o programa...')
            break
        print('Digite apenas "S" ou "N".')
