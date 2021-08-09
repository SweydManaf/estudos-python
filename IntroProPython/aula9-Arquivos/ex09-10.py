import sys
lista_nomes = sys.argv[1:]
saida = open('saida_grande.txt', 'w')
for nome in lista_nomes:
    try:
        arquivo = open(nome, 'r')
        texto = arquivo.readlines()[:]
        for str in texto:
            saida.write(str)
    except:
        print(f'{nome} -> arquivo nao encotrado')
saida.close()
