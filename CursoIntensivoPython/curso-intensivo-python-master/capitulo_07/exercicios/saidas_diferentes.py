# Primeira versão: teste condicional para encerrar.
prompt = '\nMe diga alguns ingredientes para ser adicionado na pizza.'
prompt += f"\n{'(Digite [quit] para sair do programa.)':^57}"

ingrediente = ''
while ingrediente != 'quit':
    ingrediente = input(f'{prompt}\nIngrediente: ').lower().strip()
    if ingrediente.isalpha():
        print(f'\nAdicionando {ingrediente}...')
    else:
        print('ERRO: digite o ingrediente novamente.')

# Segunda versão: variável active para controlar o tempo que o laço executará.
prompt = '\nMe diga alguns ingredientes para ser adicionado na pizza.'
prompt += f"\n{'(Digite [quit] para sair do programa.)':^57}"

active = True
while active:
    ingrediente = input(f'{prompt}\nIngrediente: ').lower().strip()
    if ingrediente.isalpha():
        if ingrediente == 'quit':
            active = False
        else:
            print(f'\nAdicionando {ingrediente}...')
    else:
        print('ERRO: digite o ingrediente novamente.')

# Terceira versão: uma instrução break para sair do laço.
prompt = '\nMe diga alguns ingredientes para ser adicionado na pizza.'
prompt += f"\n{'(Digite [quit] para sair do programa.)':^57}"

while True:
    ingrediente = input(f'{prompt}\nIngrediente: ').lower().strip()
    if ingrediente.isalpha():
        if ingrediente == 'quit':
            break
        else:
            print(f'\nAdicionando {ingrediente}...')
    else:
        print('ERRO: digite o ingrediente novamente.')
