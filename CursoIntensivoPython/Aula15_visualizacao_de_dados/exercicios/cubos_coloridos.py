import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# Define o titulo e nomeia a coordenadas
plt.title("Cubos", fontsize=24)
plt.xlabel('Valores', fontsize=14)
plt.ylabel('Valores ao cubo', fontsize=14)

# Grafico de linhas
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=40)
plt.axis([0, 5100, 0, 132500000000])

plt.show()
