import json


def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = 'nome_de_usuario.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Pede um novo nome de usuário."""
    username = input('What is your name? ')

    filename = 'nome_de_usuario.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

    return username


def greet_user():
    """Saúda o usuário pelo nome."""
    username = get_stored_username()
    if username:
        print(f'Welcome back, {username}!')
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
