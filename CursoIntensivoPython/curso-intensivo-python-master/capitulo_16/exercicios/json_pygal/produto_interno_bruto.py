import json

from pygal_maps_world.maps import World
from pygal.style import NeonStyle as NS, RotateStyle as RS

from country_codes import get_country_code


# Carrega os dados em uma lista.
filename = 'global_gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Constrói um  dicionário com o PIB das populações.
cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2014:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))

        code = get_country_code(country_name)
        if code:
            cc_gdps[code] = gdp

# Agrupa os países em três níveis de PIB.
# Menor que 5 bilhões, menor que 50 bilhões, >= 50 bilhões.
# Também converte bilhões para valores de apresentação.
cc_gdps_1, cc_gdps_2, cc_gdps_3 = {}, {}, {}
for cc, gdp in cc_gdps.items():
    if gdp < 5000000000:
        cc_gdps_1[cc] = round(gdp / 1000000000)
    elif gdp < 50000000000:
        cc_gdps_2[cc] = round(gdp / 1000000000)
    else:
        cc_gdps_3[cc] = round(gdp / 1000000000)

# Vê quantos países estão em cada nível.
print(len(cc_gdps_1), len(cc_gdps_2), len(cc_gdps_3))

wm_style = RS('#336699', base_style=NS)
wm = World(style=wm_style)
wm.title = 'Global GDP in 2014, by Country (in billions USD)'

wm.add('0-5bn', cc_gdps_1)
wm.add('5bn-50bn', cc_gdps_2)
wm.add('>50bn', cc_gdps_3)

wm.render_to_file('imagens/global_gdp.svg')
