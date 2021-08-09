import sys
if len(sys.argv) != 3:
    print('Uso ex09-08.py LARGURA LINHAS')
else:
    try:
        LARGURA = int(sys.argv[1])
        LINHA = int(sys.argv[2])
    except:
        print('Voce informou valores invalidos')
    else:

        nome_do_arquivo = 'mobydick.txt'

        def verifica_pagina(arquivo, linha, pagina):
            if(linha==linhas):
                rodape = f'= {nome_do_arquivo} - Pagina: {pagina} ='
                arquivo.write(rodape.center(LARGURA - 1) + '\n')
                pagina += 1
                linha = 1
            return linha, pagina


        def escreve(arquivo, linha, nlinhas, pagina):
            arquivo.write(linha+'\n')
            return verifica_pagina(arquivo, nlinhas, pagina)


        entrada = open(nome_do_arquivo, encoding='utf-8')
        saida = open('saida_paginada.txt', 'w', encoding='utf-8')

        pagina = 1
        linhas = 1

        for linha in entrada.readlines():
            palavras = linha.rstrip().split(" ")
            linha = ''
            for p in palavras:
                p = p.strip()
                if len(linha) + len(p) + 1 > LARGURA:
                    linhas, pagina = escreve(saida, linha, linhas, pagina)
                    linha = ''
                linha += p+''
            if(linha != ''):
                linhas, pagina = escreve(saida, linha, linhas, pagina)

        while(linhas!=1):
            linhas, pagina = escreve(saida, '', linha, pagina)

        entrada.close()
        saida.close()