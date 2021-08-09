from CursoIntensivoPython.Aula15_visualizacao_de_dados.die import Die
import pygal
from pygal.style import NeonStyle

# Cria dois dados
die_1 = Die()
die_2 = Die()

# Armazena os lancamentos dos dados
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# Analisa a frequencia dos resultados
max_results = die_1.num_sides + die_2.num_sides
frequency = [results.count(value) for value in range(1, max_results+1)]

# Plota os dados num grafico de baras
hist = pygal.Bar(style=NeonStyle)
hist.title = 'Multiplicacao dos lancamentos do dados D6 1000 vezes.'
hist.x_labels = list(range(1, max_results+1))
hist.x_title = 'Resultados'
hist.y_title = 'Frequencia dos resultados'

hist.add('D6 x D6', frequency)
hist.render_to_file('multiplicacao.svg')