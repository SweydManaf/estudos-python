pessoa = {
    'primeiro_nome': 'william',
    'ultimo_nome': 'rodrigues',
    'idade': 19,
    'cidade': 'ceará',
    }

for k, v in pessoa.items():
    print(f'\nChave: {k}\nValor: {str(v).title()}')
