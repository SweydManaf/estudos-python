cidades = {'rio de janeiro': {'pais': 'brasil',
                              'populacao': 16718956,
                              'fato': 'É o terceiro estado mais populoso do Brasil'},
           'paris': {'pais': 'frança',
                     'populacao': 2206488,
                     'fato': 'É considerada uma das mais importantes do mundo'},
           'washington': {'pais': 'estados unidos',
                          'populacao': 7405743,
                          'fato': 'A primeira escola de Washington foi fundada em 1832'},
           }

for cidade, info in cidades.items():
    print(f'\nCidade: {cidade.title()}')
    print(f'\tPaís: {info["pais"].title()}\n'
          f'\tPopulação: {info["populacao"]:,} de habitantes aproximadamente.\n'
          f'\tFato: {info["fato"]}.')
