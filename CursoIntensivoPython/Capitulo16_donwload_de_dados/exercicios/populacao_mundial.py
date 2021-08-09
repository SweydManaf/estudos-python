import pygal
import json

# Obtem os dados necessarios
filename = open('population_data.json')
with filename as f:
    data = json.load(f)

    years, populations = [], []
    pop = {}
    for pop_dict in data:
        year = pop_dict['Year']
        years.append(year)
        pop[year] = 0

    for year in years:
        for pop_dict in data:
            if pop_dict['Year'] == year:
                pop[year] += int(float(pop_dict['Value']))

# Monta o histograma da populacao
hist = pygal.Line()
hist.title = 'World Population'
hist.x_labels = [int(k) for k in pop.keys()]
hist.x_title = 'Years'
hist.y_title = 'Global Population'

hist.add('World Population', [v for v in pop.values()])
hist.render_to_file('world.svg')
