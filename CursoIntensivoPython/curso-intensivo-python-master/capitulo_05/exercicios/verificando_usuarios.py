usuarios_atuais = ['marcela', 'pedro', 'william', 'joão', 'paulo']
novos_usuarios = ['kelly', 'PEDRO', 'João', 'iago', 'igor']

for usuario in novos_usuarios:
    if usuario.lower() in usuarios_atuais:
        print(f'O nome de usuário {usuario} já está em uso, forneça um novo.')
    else:
        print(f'O nome de usuário {usuario} está disponível!')
