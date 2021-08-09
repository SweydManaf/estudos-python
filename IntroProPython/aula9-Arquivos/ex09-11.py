arquivo = open('mobydick.txt', 'r')
texto = arquivo.readlines()[:]
tam = len(texto)
dicionario = dict()


for linha in texto:
    linha = linha.strip().lower()
    palavras = linha.split()
    for p in palavras:
        if p in dicionario:
            dicionario[p] += 1
        else:
            dicionario[p] = 1

print(dicionario)
arquivo.close()

#Sweetn Soluction