import sys

tam = len(sys.argv) - 1

for a in sys.argv[1:]:
    try:
        arquivo = open(a, 'r')
    except:
        print(f'{a}: Arquivo nao encotrado')
    else:
        for linha in arquivo.readlines():
            print(linha[:-1])
        input('Digite Enter para continuar')