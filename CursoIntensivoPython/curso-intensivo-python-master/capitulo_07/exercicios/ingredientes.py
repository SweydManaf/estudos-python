prompt = '\nMe diga alguns ingredientes para ser adicionado na pizza.'
prompt += f"\n{'(Digite [quit] para sair do programa.)':^57}"

ingrediente = ''
while ingrediente != 'quit':
    ingrediente = input(f'{prompt}\nIngrediente: ').lower().strip()
    if ingrediente.isalpha():
        print(f'\nAdicionando {ingrediente}...')
    else:
        print('ERRO: digite o ingrediente novamente.')
