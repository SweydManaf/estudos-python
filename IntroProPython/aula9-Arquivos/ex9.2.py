import sys

if len(sys.argv) != 4:
    print('Uso ex9-1.py nome_do_arquivo inicio fim')
else:
    try:
        nome_arquivo = sys.argv[1]
        arquivo = open(nome_arquivo, 'r')
    except:
        print('\033[31mERRO: arquivo inexistente no directorio actual!')
    else:
        inicio = int(sys.argv[2]) - 1
        fim = int(sys.argv[3])
        cont = 0
        for linha in arquivo.readlines():
            if inicio <= cont <= fim:
                print(linha[:-1])
            cont += 1
            if cont == fim:
                break
        arquivo.close()

#Melhor solucao
'''
for linha in arquivo.readlines()[inicio:fim]:
    print(linha[:-1])
arquivo.close()
'''