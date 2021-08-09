usuarios = []

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print(f'Olá admin, gostaria de ver um relatório de status?')
        else:
            print(f'Olá {usuario.title()}, obrigado por fazer login novamente.')
else:
    print('Precisamos encontrar alguns usuários!')
