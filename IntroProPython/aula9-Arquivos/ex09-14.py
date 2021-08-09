arquivo =open('mobydick.txt', 'r')
saida = open('saida.txt', 'w')
texto = arquivo.readlines()[:]
for linha in texto:
    if linha == '\n':
        continue
    else:
        linha = linha.split()
    for palavra in linha:
        saida.write(f'{palavra} ')
    saida.write('\n')


arquivo.close()
saida.close()