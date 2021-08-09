import matplotlib.pyplot as plt
from CursoIntensivoPython.Aula15_visualizacao_de_dados.die import Die


# Cria os dados
dado_1 = Die()
dado_2 = Die()

# Armazena os resultados dos lancamentos dos dados
results = [dado_1.roll() + dado_2.roll() for num_roll in range(1000)]

# Frequencia dos resultados
max_results = dado_1.num_sides + dado_2.num_sides
values_y = [results.count(value) for value in range(2, max_results+1)]
value_x = list(range(2, max_results+1))

# Plota os dados
plt.title("Lancamento de dois dados")
plt.xlabel('Resultados')
plt.ylabel('Frequencia dos resultados')
plt.bar(value_x, values_y)
plt.show()
