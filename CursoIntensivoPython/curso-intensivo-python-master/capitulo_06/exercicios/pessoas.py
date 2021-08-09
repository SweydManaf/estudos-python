pessoa_0 = {
    'primeiro_nome': 'william',
    'ultimo_nome': 'rodrigues',
    'idade': 19,
    'cidade': 'ceará',
    }
pessoa_1 = {
    'primeiro_nome': 'kelly',
    'ultimo_nome': 'alves',
    'idade': 20,
    'cidade': 'rio de janeiro',
    }
pessoa_2 = {
    'primeiro_nome': 'raimundo',
    'ultimo_nome': 'rodrigues',
    'idade': 48,
    'cidade': 'ceará',
    }

pessoas = [pessoa_0, pessoa_1, pessoa_2]
for pessoa in pessoas:
    nome_completo = f'{pessoa["primeiro_nome"]} {pessoa["ultimo_nome"]}'
    print(f'\nNome completo: {nome_completo.title()}')
    for k in pessoa.keys():
        if k == 'idade':
            print(f'\tIdade: {pessoa[k]}')
        if k == 'cidade':
            print(f'\tCidade: {pessoa[k].title()}')
