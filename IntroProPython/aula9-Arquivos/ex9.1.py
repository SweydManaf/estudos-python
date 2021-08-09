import sys

if len(sys.argv) != 2:
    print('Uso ex9-1.py nome_do_arquivo')
else:
    try:
        nome_arquivo = sys.argv[1]
        arquivo = open(nome_arquivo, 'r')
    except:
        print('\033[31mERRO: arquivo inexistente no directorio actual!')
    else:
        for linha in arquivo.readlines():
            print(linha[-1])
        arquivo.close()