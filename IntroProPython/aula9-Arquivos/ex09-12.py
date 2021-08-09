#Nilo soluction

arquivo = open('mobydick.txt', 'r')
texto = arquivo.readlines()[:]
tam = len(texto)
dicionario = dict()
lista = list()
clinha = 1
coluna = 1


for linha in texto:
    linha = linha.strip().lower()
    palavras = linha.split()
    for p in palavras:
        if p == '':
            coluna += 1

        if p in dicionario:
            dicionario[p].append((clinha, coluna))
        else:
            dicionario[p] = [clinha, coluna]
        coluna += len(p)+1
    clinha += 1
    coluna = 1
for k, v in dicionario.items():
    print(f'{k} = {v}')
arquivo.close()
