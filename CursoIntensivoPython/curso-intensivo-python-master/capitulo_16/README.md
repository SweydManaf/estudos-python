# Referências Rápidas do Capítulo

- ### Utilização do [_matplotlib_](https://matplotlib.org/) e da biblioteca padrão do Python para arquivos [_.csv_](https://docs.python.org/3/library/csv.html)
Exemplo de gráfico para visualizar as temperaturas máximas e mínimas do ano de 2014 da cidade de Sitka, AK.
>- [_highs_lows.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/highs_lows.py) | [_sitka_weather_2014.csv_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/sitka_weather_2014.csv)

```
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime


# Obtém as datas e as temperaturas máximas e mínimas do arquivo.
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d').date()

            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'Missing data.')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Faz a plotagem dos dados.
fig = plt.figure(dpi=128, figsize=(10, 6))

# Formata xaxis com 1 mês de intervalo e o formato da data.
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formata o gráfico.
title = 'Daily high and low temperatures - 2014\nSitka, AK'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)


plt.savefig('imagens/highs_lows_sitka.png')
plt.show()
```

<img src='https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/imagens/highs_lows_sitka.png' heigth='830' width='700'>

Gráfico utilizando o mesmo código porém com o arquivo do ano de 2014 da cidade de Death Valley, CA.
>- [_highs_lows.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/highs_lows.py) | [_death_valley_2014.csv_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/death_valley_2014.csv)

<img src='https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/imagens/highs_lows_dv.png' heigth='830' width='700'>

---

- ### Utilização do [_Pygal_](pygal.org) com a biblioteca padrão do Python para arquivos [_.json_](https://docs.python.org/3/library/json.html)
Para criar imagens representativas do mapa-múndi com o Pygal é necessário instalar o módulo `pygal_maps_world`, para isso usamos o pip:
> `$ pip install --user pygal_maps_world` 

No Windows:

> `$ python -m pip install --user pygal_maps_world`


Importamos o dicionário COUNTRIES e criamos uma função para pegar as duas siglas para cada país, pois o Pygal só aceita esse formato.
>- [_country_codes.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/country_codes.py)

Agora é só iniciar a representação, primeiro usaremos as 3 Américas, do Norte, Central e do Sul e seus principais países.
>- [_americas.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/americas.py)

```
from pygal_maps_world.maps import World
from pygal.style import NeonStyle


wm = World(style=NeonStyle)
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('imagens/americas.svg')
```

<img src='https://user-images.githubusercontent.com/47596121/66001037-09e8be80-e477-11e9-96de-2633ecf98b93.png' heigth='830' width='700'>

Verificando a população de cada país da América do Norte: México, Estados Unidos e Canadá usando uma representação com o Pygal.
>- [_na_populations.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/na_populations.py)

```
from pygal_maps_world.maps import World
from pygal.style import NeonStyle

wm = World(style=NeonStyle)
wm.title = 'Populations of Countries in North America'

wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('imagens/na_populations.svg')
```

<img src='https://user-images.githubusercontent.com/47596121/66001721-7b753c80-e478-11e9-98ce-860569a01512.png' heigth='830' width='700'>

Finalmente, utilizando o arquivo `population_data.json` para pegar dados (de 2010) de todos os países e criar um mapa-mundí completo com
informação populacional de cada um dos países e representar no Pygal. 
> Alguns países ficaram de fora, mas todos os que estão no diconário `COUNTRIES` foram adicionados nessa representação.

>- [_world_population.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/world_population.py) | [_population_data.json_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/population_data.json)

```
import json

from pygal_maps_world.maps import World
from pygal.style import NeonStyle as NS, RotateStyle as RS

from country_codes import get_country_code


# Carrega os dados em uma lista.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Constrói um  dicionário com dados das populações.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))

        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Agrupa os países em três níveis populacionais.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Vê quantos países estão em cada nível.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=NS)
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'

wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('imagens/world_population.svg')
```

<img src='https://user-images.githubusercontent.com/47596121/66002424-0efb3d00-e47a-11e9-8ccf-f6bacb5073d6.png' heigth='830' width='700'>

> [_NeonStyle_](http://pygal.org/en/stable/documentation/builtin_styles.html#neon) do Pygal.

---
