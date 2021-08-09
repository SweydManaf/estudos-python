import cidade_funcoes as cf

while True:
    cidade = str(input('\nDigite o nome da cidade: ')).strip()
    pais = str(input('Digite o nome do país: ')).strip()

    while True:
        resposta = str(input(
            f'\nDeseja colocar a população de {cidade.title()}? [S/N] '
        )).upper().strip()

        if resposta in 'SN' and resposta != '':
            if resposta == 'S':
                try:
                    populacao = int(input(
                        'Digite o número da população: '))
                except ValueError:
                    continue
                else:
                    cpp = cf.cidade_pais(cidade, pais, populacao)
                    print(f'\n\tNome formatado: {cpp}\n')
            else:
                cp = cf.cidade_pais(cidade, pais)
                print(f'\n\tNome formatado: {cp}\n')
            break

        print('Digite apenas "S" ou "N".')

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if continuar in 'SN' and continuar != '':
            break
        print('Digite apenas "S" ou "N".\n')

    if continuar == 'N':
        break
