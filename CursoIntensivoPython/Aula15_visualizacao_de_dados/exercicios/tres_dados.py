from CursoIntensivoPython.Aula15_visualizacao_de_dados.die import Die
import pygal
import pygal.style as pystyle

# Cria os dados
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Armazena os lancamentos dos dados 1000
results = [die_1.roll() + die_2.roll() + die_3.roll() for num in range(1000)]

# Analisa a frequencia dos resultados
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequency = [results.count(value) for value in range(3, max_results+1)]

# Plota o grafico de baras
hist = pygal.Dot(style=pystyle.DarkGreenStyle)
hist.title = 'LANCAMENTO DE D6x3 1000 vezes.'
hist.x_labels = list(range(3, max_results+1))
hist.x_title = 'Resultado'
hist.y_title = 'Frequencia dos resultados'

hist.add('D6 + D6 + D6', frequency)
hist.render_to_file('tres_dados.svg')
