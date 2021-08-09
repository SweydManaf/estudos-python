import json


def obter_username_armazenado() -> str or None:
    """
    -> Obtém o nome do usuário já
    armazenado se estiver disponível.

    :return: Retorna o nome do usuário.
    """
    arquivo = 'arquivos_json/nome_de_usuario.json'
    try:
        with open(arquivo) as obj_arq:
            username = json.load(obj_arq)
    except FileNotFoundError:
        return None
    else:
        return username


def obter_novo_username() -> str:
    """
    -> Pede um novo nome de usuário.

    :return: Retorna o novo nome de usuário.
    """
    username = input('Qual é o seu nome? ')

    arquivo = 'arquivos_json/nome_de_usuario.json'
    with open(arquivo, 'w') as obj_arq:
        json.dump(username, obj_arq)

    return username


def saudar_usuario():
    """Saúda o usuário pelo nome."""
    usuario = obter_username_armazenado()
    if usuario:
        while True:
            prompt = f'{usuario} é o seu nome de usuário? [S/N] '
            usuario_correto = str(input(prompt)).upper().strip()
            if usuario_correto in 'SN':
                if usuario_correto == 'S':
                    print(f'Bem-vindo novamente, {usuario}!')
                else:
                    usuario = obter_novo_username()
                    print(f"Lembraremos de você quando retornar, {usuario}!")
                break
    else:
        usuario = obter_novo_username()
        print(f"Lembraremos de você quando retornar, {usuario}!")


saudar_usuario()
