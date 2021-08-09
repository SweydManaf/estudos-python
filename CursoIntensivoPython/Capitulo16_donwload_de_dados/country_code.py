from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Devolve o codigo de duas letras do pygal para um pais,
    dado o seu nome."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            print(f'{name} = {country_name}')
            return code
        elif name in country_name:
            print(f'{name} -- {country_name}')
            return code
    # Se o pais nao foi encontrado, devolve None
    return None
