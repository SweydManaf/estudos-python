def city_fuctions(city, country, population=''):

    city = city.title()
    country = country.title()

    if population:
        nome = f'{city}, {country} - populacao {population}'
    else:
        nome = f'{city}, {country}'
    return nome