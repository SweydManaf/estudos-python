from time import sleep

linguagens = ['java', 'c', 'python', 'javascript',
              'r', 'perl', 'ruby', 'assembly']
linguagens_copia = linguagens[:]

while True:
    while True:
        linguagem = str(input('\nQual a sua linguagem favorita? ')).lower().strip()
        if linguagem.isnumeric() or linguagem == '':
            print('\033[1;31mERRO: digite a linguagem novamente.\033[m')
        else:
            break
    nova_linguagem = f'{linguagem} [nova]'
    nova_linguagem_existente = f'{linguagem} [nova]'.upper()

    cond1 = linguagem in linguagens_copia
    cond2 = nova_linguagem in linguagens_copia
    cond3 = nova_linguagem_existente in linguagens_copia
    if cond1 or cond2 or cond3:
        print('\033[1;31mOps, parece que alguém já escolheu essa linguagem.\033[m')
        while True:
            escolher = str(input('\nDeseja removê-la e colocar a sua no lugar? [S/N] ')).upper()[0]
            if escolher in 'SN':
                if escolher == 'S':
                    print('Trocando as linguagens de lugar, espere um instante...')
                    sleep(2)
                    print('Removendo a linguagem antiga...')
                    sleep(2)
                    # Letra maiúscula significa que a linguagem foi trocada.
                    if cond2:
                        linguagens_copia.insert(
                            linguagens_copia.index
                            (nova_linguagem), nova_linguagem.upper()
                        )
                        linguagens_copia.remove(nova_linguagem)
                    elif cond3:
                        linguagens_copia.insert(
                            nova_linguagem_existente.index
                            (nova_linguagem_existente), nova_linguagem_existente
                        )
                        linguagens_copia.remove(nova_linguagem_existente)
                    else:  # cond1
                        linguagens_copia.insert(
                            linguagens_copia.index
                            (linguagem), linguagem.upper()
                        )
                        linguagens_copia.remove(linguagem)
                    print('\033[1;34mPRONTO!\033[m')
                else:
                    print('\033[1;34mTudo bem! Prosseguindo com o programa...\033[m')
                    sleep(2)
                break
            print('\033[1;31mDigite apenas S ou N.\033[m')
    else:
        print('\033[1;34mLinguagem adicionada com sucesso!\033[m')
        linguagens_copia.append(f'{linguagem} [Nova]'.lower())

    while True:
        continuar = str(input('\nDeseja adicionar mais linguagens? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('\033[1;31mDigite apenas S ou N.\033[m')
    if continuar == 'N':
        break

print(f'\nLista das linguagens favoritas original ordenada:')
for linguagem in sorted(linguagens):
    print(f'\t\033[1;34m{linguagem.title()}\033[m')
print(f'\nLista das linguagens favoritas alterada ordenada:')
for linguagem in sorted(linguagens_copia, key=str.lower):
    if linguagem.isupper():
        # Vermelho para a linguagem alterada ou uma nova linguagem que foi alterada.
        print(f'\t\033[1;31m{linguagem.title()}\033[m')
    else:
        # Azul para nova linguagem ou a que não foi alterada.
        print(f'\t\033[1;34m{linguagem.title()}\033[m')
