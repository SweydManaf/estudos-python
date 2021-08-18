market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


def switchLights(spotlight):
    for key in spotlight.keys():
        if spotlight[key] == 'green':
            spotlight[key] = 'yellow'
        elif spotlight[key] == 'yellow':
            spotlight[key] = 'red'
        elif spotlight[key] == 'red':
            spotlight[key] = 'green'

    assert 'red' in spotlight.values(), f'Neither light is red! {spotlight}'

switchLights(market_2nd)