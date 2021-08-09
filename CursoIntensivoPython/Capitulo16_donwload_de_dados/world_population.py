import json
from pygal_maps_world.maps import World
from pygal import style
from CursoIntensivoPython.Capitulo16_donwload_de_dados.country_code import get_country_code

# Carrega os dados em uma lista
filename = open('population_data.json')
with filename as f:
    pop_data = json.load(f)

# Constroi um dicionario com dados das populacoes
cc_populations = {}
errados = 0
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population


# Agrupa os paises em tres niveis populacionais
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Ve quantos paises estao em cada nivel
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = style.TurquoiseStyle
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
