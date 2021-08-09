nomes = ['Iago', 'Igor', 'Milly', 'Iury', 'Rafael', 'Ronaldo', 'Vinicius']

for nome in nomes:
    print(nome, end=', ' if nome != nomes[-1] else '.')
