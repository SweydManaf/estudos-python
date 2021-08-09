termos = {
    'concatenação': 'juntar duas ou mais sequências de caracteres',
    'indentação': 'significa o recuo de um texto em relação a sua margem esquerda',
    'iteração': 'nome das estruturas que repetem um mesmo bloco de código enquanto True',
    'string': 'conjunto de caracteres numa determinada ordem',
    'compilação': 'converter código fonte de programação em código executável',
    }

for palavra, significado in termos.items():
    print(f'{palavra.title()}:\n\t{significado.capitalize()}.\n')
