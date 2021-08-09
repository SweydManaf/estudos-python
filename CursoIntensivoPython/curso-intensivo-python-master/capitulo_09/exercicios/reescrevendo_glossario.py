from collections import OrderedDict

termos = OrderedDict()
termos['indentação'] = 'significa o recuo de um texto em relação a sua margem esquerda'
termos['string'] = 'conjunto de caracteres numa determinada ordem'
termos['iteração'] = 'nome das estruturas que repetem um mesmo bloco de código enquanto True'
termos['compilação'] = 'converter código fonte de programação em código executável'
termos['concatenação'] = 'juntar duas ou mais sequências de caracteres'

for palavra, significado in termos.items():
    print(f'{palavra.title()}:\n\t{significado.capitalize()}.\n')
