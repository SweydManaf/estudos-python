from CursoIntensivoPython.Aula15_visualizacao_de_dados.die import Die
import pygal
from pygal.style import DarkColorizedStyle

# Cria os dados
die_1 = Die(8)
die_2 = Die(8)

# Armazena os resultados dos lancamentos
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Frequencia dos lancamentos
max_results = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_results+1)]

# Plota os dados em grafico de baras
hist = pygal.Bar(style=DarkColorizedStyle)

hist.title = "Lancamentos de D8 1000 vezes."
hist.x_labels = list(range(2, max_results+1))
hist.x_title = 'Resultado'
hist.y_title = 'Frequencia dos resultados'

hist.add('D8 + D8', frequencies)
hist.render_to_file('dois_d8s.svg')