par = open('pares.txt', 'r')
inverso = par.readlines()[::-1]

saida = open('pares_invertido.txt', 'w')
verso = inverso[:]

for c in range(0, len(verso)):
    saida.write(f'{verso[c]}')

saida.close()
par.close()

'''
Nilo soluction:  

L = pares.readlines()
L.reverse()
 
'''