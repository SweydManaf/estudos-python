import pygal
from pygal.style import NeonStyle

from die import Die


# Cria dois dados D6.
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista.
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# Analisa os resultados.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

# Visualiza os resultados.
hist = pygal.Bar(style=NeonStyle)
hist.force_uri_protocol = 'http'

hist.title = 'Results of rolling two D6 mul 1000 times.'
hist.x_labels = [x for x in range(1, max_result + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6 * D6', frequencies)

hist.render_to_file('imagens/mul_dados.svg')
