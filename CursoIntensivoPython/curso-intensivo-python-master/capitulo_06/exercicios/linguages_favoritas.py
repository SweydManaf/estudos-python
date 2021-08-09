linguagens_favoritas = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'will': 'python',
    'clau': 'perl',
    'belly': 'php',
    }
nomes = ['phil', 'will', 'erin', 'iago', 'clau']

for nome in nomes:
    if nome in linguagens_favoritas.keys():
        print(f'{nome.title()}, muito obrigado por ter respondido a nossa enquete!')
    else:
        print(f'{nome.title()}, você gostaria de responde a nossa enquete?')
