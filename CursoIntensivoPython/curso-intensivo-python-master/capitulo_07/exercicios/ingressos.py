prompt = '\n\tVerifique o preço dos ingressos para o cinema aqui.'
prompt += f"\nDigite sua idade: "

while True:
    try:
        idade = int(input(prompt))
    except (ValueError, TypeError):
        print('ERRO: digite um número inteiro para a sua idade.')
    else:
        if idade > 0:
            if idade < 3:
                ingresso = 'US$00.00'
            elif idade <= 12:
                ingresso = 'US$10.00'
            else:
                ingresso = 'US$15.00'
            if idade != 1:
                print(f'\nIdade: {idade} anos'
                      f'\nPreço: {ingresso}')
            else:
                print(f'\nIdade: {idade} ano'
                      f'\nPreço: {ingresso}')
            while True:
                pergunta = str(input('\nDeseja continuar?\n[S/N] ')).upper().strip()
                if pergunta.isalpha():
                    if pergunta in 'SN':
                        break
                print('Digite apenas "S" ou "N".')
            if pergunta == 'N':
                print('\n\tObrigado pela preferência, volte sempre!')
                break
        else:
            print('Digite uma idade válida maior que 0.')
