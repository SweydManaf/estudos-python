import requests
import bs4

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.78873500000003&lon=-122.3945#.YgJD_rWHvhZ')
res.raise_for_status()

BioSoup = bs4.BeautifulSoup(res.text, features='html.parser')
weatherSoup = BioSoup.select('.myforecast-current-lrg')


print(weatherSoup[0].getText())