import json

filename = 'nome_de_usuario.json'

with open(filename) as f_obj:
    username = json.load(f_obj)

print(f'Welcome back, {username}!')
