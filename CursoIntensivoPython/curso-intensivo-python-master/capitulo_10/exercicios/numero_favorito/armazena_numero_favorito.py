import json

arquivo = '../arquivos_json/numero_favorito.json'

try:
    numero = int(input('Qual é o seu número favorito? '))
except ValueError:
    print('ERRO: digite um número inteiro válido.')
else:
    try:
        with open(arquivo, 'w') as obj_arq:
            json.dump(numero, obj_arq)
    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não existe.")
    else:
        print('O seu número favorito foi armazenado com sucesso.')
