import json

arquivo = '../arquivos_json/numero_favorito.json'

try:
    with open(arquivo) as obj_arq:
        numero = json.load(obj_arq)
except FileNotFoundError:
    print(f"O arquivo '{arquivo}' não existe.")
else:
    print(f'Eu sei qual é o seu número favorito! É {numero}.')
