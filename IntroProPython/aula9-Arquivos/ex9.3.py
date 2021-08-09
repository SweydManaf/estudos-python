# Nilo Soluction

def le_numero(arquivo):
    while True:
        numero = arquivo.readline()
        if numero == "":
            return None
        if numero.strip()!="":
            return int(numero)


def escreve_numero(arquivo, n):
    arquivo.write(f'{n}\n')


par = open('pares.txt', 'r')
impar = open('impares.txt', 'r')
pareimpar = open('pareseimpares.txt', 'w')
npar = le_numero(par)
nimpar = le_numero(impar)

while True:
    if npar == None and nimpar == None:
        break
    if npar != None and (nimpar==None or npar <= nimpar):
        escreve_numero(pareimpar, npar)
        npar = le_numero(par)
    if npar != None and (npar == None or nimpar <=npar):
        escreve_numero(pareimpar, nimpar)
        nimpar = le_numero(impar)

pareimpar.close()
par.close()
impar.close()