import sys

if len(sys.argv) != 4:
    print('Uso ex09-13.py nome_do_aquivo inicio fim')
else:
    try:
        nome = sys.argv[1]
        arquivo = open(nome, 'r')
        inicio = int(sys.argv[2])
        fim = int(sys.argv[3])
    except:
        print(f'{nome} -> arquivo nao encontrado.')
    else:
        c = 1
        for linha in arquivo.readlines()[inicio-1: fim]:
            print(linha[:-1])