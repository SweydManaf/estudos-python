#Exercicio 8.15
'''
Dica: envie o nível atual como parâmetro e utilize-o para calcular a
quantidade de espaços em branco à esquerda de cada elemento
#Dica nao usada
'''


L = [1, [2, 3, 4, [5, 6, 7]]]
for e in L:
    if type(e) == list:
        for i in e:
            if type(i) == list:
                for a in i:
                    print('  ', a)
            elif type(i) == int:
                print(' ', i)
    elif type(e) == int:
        print(e)
