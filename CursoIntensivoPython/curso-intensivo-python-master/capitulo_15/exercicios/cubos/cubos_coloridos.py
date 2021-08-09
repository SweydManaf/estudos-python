import matplotlib.pyplot as plt


# Escolhe os valores de entrada e seus respectivos cubos e plota eles.
valores_x = list(range(1, 5001))
valores_y = [x ** 3 for x in valores_x]
plt.scatter(valores_x, valores_y, c=valores_y, cmap=plt.cm.Oranges, edgecolors='none', s=20)

# Define o título do gráfico e de seus eixos.
plt.title('Cubo dos Números', fontsize=24)
plt.ylabel('Cubo do Valor', fontsize=14)
plt.xlabel('Valores', fontsize=14)

# Define o tamanho dos rótulos das marcações.
plt.tick_params(axis='both', which='major', labelsize=12)

# Defina o valo para cada eixo.
plt.axis([0, 5100, 0, 132500000000])

plt.savefig('imagens/cubos_coloridos.png', bbox_inches='tight')
plt.show()
