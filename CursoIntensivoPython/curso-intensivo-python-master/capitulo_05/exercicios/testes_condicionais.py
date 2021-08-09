carro = 'subaru'
print(f"carro == 'subaru'? Eu chuto True.\n{carro == 'subaru'}")
print(f"carro == 'audi'? Eu chuto False.\n{carro == 'audi'}")

sorvete = 'baunilha'
print(f"\nsorvete == 'baunilha'? Eu chuto True.\n{sorvete == 'baunilha'}")
print(f"sorvete == 'morango'? Eu chuto False.\n{sorvete == 'morango'}")

carros = ['chevrolet', 'bmw', 'fiat', 'ferrari']
print(f"\n'bmw' in carros? Eu chuto True.\n{'bmw' in carros}")
print(f"'fiat' not in carros? Eu chuto False.\n{'fiat' not in carros}")

cidade = 'rio de janeiro'
print(f"\ncidade == 'rio de janeiro'? Eu chuto True.\n{cidade == 'rio de janeiro'}")
print(f"cidade != 'rio de janeiro'? Eu chuto False.\n{cidade != 'rio de janeiro'}")

idade = 18
print(f"\nidade >= 18? Eu chuto True.\n{idade >= 18}")
print(f"idade > 18? Eu chuto False.\n{idade > 18}")

idade = 19
print(f"\nidade <= 19? Eu chuto True.\n{idade <= 19}")
print(f"idade < 19? Eu chuto False.\n{idade < 19}")

cidades = ['ceará', 'rio de janeiro', 'bahia', 'minas gerais']
print(f"\n'ceará' in cidades? Eu chuto True.\n{'ceará' in cidades}")
print(f"'ceará' not in cidades? Eu chuto False.\n{'ceará' not in cidades}")
print(f"\n'rio de janeiro' in cidades? Eu chuto True.\n{'rio de janeiro' in cidades}")
print(f"'rio de janeiro' not in cidades? Eu chuto False.\n{'rio de janeiro' not in cidades}")

nomes = ['IAGO', 'MILLY', 'IGOR', 'MARCUS']
print(f"\n'IAGO' == 'iago'.upper()? Eu chuto True.\n{nomes[0] == 'iago'.upper()}")
print(f"'MILLY' == 'MILLY'.lower()? Eu chuto False.\n{nomes[1] == 'MILLY'.lower()}")

numeros = [10, 6, 4, 8, 12]
print(f"\n10 >= 6 + 4? Eu chuto True.\n{numeros[0] >= numeros[1] + numeros[2]}")
print(f"10 < 8? Eu chuto False.\n{numeros[0] < numeros[3]}")
print(f"\n12 and 4 + 8 > 10? Eu chuto True.\n{numeros[-1] and numeros[2] + numeros[3] > numeros[0]}")
print(f"10 > 12 or 8 > 12? Eu chuto False.\n{numeros[0] > numeros[-1] or numeros[3] > numeros[-1]}")
