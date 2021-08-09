import sys

if len(sys.argv) != 3:
    print('Uso ex09-04.py nome_arquivo_1 nome_arquivo_2')
else:
    try:
        arquivo1 = open(sys.argv[1])
        arquivo2 = open(sys.argv[2])
        saida = open('saida.txt', 'w')
    except:
        print('Arquivo nao encotrado')
    else:
        for linha1 in arquivo1.readlines():
            saida.write(f'{linha1[:-1]}\n')

        for linha2 in arquivo2.readlines():
            saida.write(f'{linha2[:-1]}\n')
        print('ARQUIVOS UNIDOS')

        arquivo1.close()
        arquivo2.close()
        saida.close()
