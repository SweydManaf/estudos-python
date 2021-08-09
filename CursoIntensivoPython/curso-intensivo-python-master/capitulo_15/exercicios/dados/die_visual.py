import pygal
from pygal.style import NeonStyle

from die import Die


# Cria um D6.
die = Die()

# Faz alguns lançamentos e armazena os resultado em uma lista.
results = [die.roll() for roll_num in range(1000)]

# Analisa os resultados.
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

# Visualiza os resultados.
hist = pygal.Bar(style=NeonStyle)
hist.force_uri_protocol = 'http'

hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = [x for x in range(1, die.num_sides + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6', frequencies)

hist.render_to_file('imagens/die_visual.svg')
