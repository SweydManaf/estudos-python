# Visualizacao de dados em Python

import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

titulo = 'Grafico de barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Legedas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y)
plt.show()
