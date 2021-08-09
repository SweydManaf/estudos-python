from time import sleep

import modulo_arquivos as ma

arquivo = 'arquivos_de_texto/respostas_da_enquete.txt'

while True:
    print(f'\n{"=-=" * 10}'
          f'\n{"ENQUETE SOBRE PROGRAMAÇÃO":^30}'
          f'\n{"=-=" * 10}')
    while True:
        nome = str(input('Qual é o seu nome? ')).strip().title()
        if nome.replace(' ', '').isalpha() and nome != '':
            break
        print('Por favor, digite seu nome novamente.')

    while True:
        prompt = f'\n{nome}, porque você gosta de programação?'
        prompt += "\n(Digite 'sair' se não quiser responder.)"
        resposta = str(input(f'{prompt}\nResposta: ')).strip().lower()

        if resposta != '':
            break
        print('Por favor, digite a resposta novamente.\n')

    if resposta == 'sair':
        print(f'\n\tTudo bem {nome}, desculpe pelo incomodo.\n')
        sleep(1)
    else:
        ma.escrever_info_enquete(arquivo, nome, resposta)

    while True:
        continuar = str(input(
            '\nDeseja continuar a enquete? [S/N] ')).strip().upper()
        if continuar in 'SN' and continuar != '':
            sleep(1)
            break
        print('Digite apenas "S" ou "N".')

    if continuar == 'N':
        print('\nFinalizando...')
        sleep(2)
        break

print(f'\n{"=-=" * 10}'
      f'\n{"RESULTADOS DA ENQUETE":^30}'
      f'\n{"=-=" * 10}')
linhas = ma.ler_arquivo(arquivo)
if linhas:
    for i, linha in enumerate(linhas):
        infos = linha.split(', ')
        sleep(1)
        print(f'{i + 1}° entrevistado:'
              f'\n\tNome: {infos[0]}'
              f'\n\tResposta: {infos[1]}'
              f'\n\tData e horário da resposta: {infos[2]}, {infos[3]}')
else:
    print(f"\nDesculpe, o arquivo '{arquivo}' não existe.")
