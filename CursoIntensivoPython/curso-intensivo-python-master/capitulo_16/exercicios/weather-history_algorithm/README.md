# Fork [_daqui_](https://github.com/fivethirtyeight/data/tree/master/us-weather-history).
Esse é um algoritimo utilizado para pegar o csv com o histórico climático de uma determinada data do site 
[_Weather Underground_](http://wunderground.com/). É utilizado [nesse artigo](https://fivethirtyeight.com/features/what-12-months-of-record-setting-temperatures-looks-like-across-the-u-s/)
do site [_FiveThirtyEight_](https://fivethirtyeight.com/).

# Notas
- Fiz algumas alterações para fornecer os parâmetros `begin_date` e `end_date` na chamada das funções.
- Use os formatos das datas assim: **'YYYY-M'**
- Utilize as funções da seguinte forma:
>- **Exemplo de entrada**: 
```
begin_date = '2014-1'
end_date = '2014-12'
station = 'KSFO'
```
>- [`wunderground_scraper_wl.py`](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/exercicios/weather-history_algorithm/wunderground_scraper_wl.py)

> ![image](https://user-images.githubusercontent.com/47596121/65840120-38399300-e2eb-11e9-9a02-f7990b220065.png)

>- [`wunderground_parser_wl.py`](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/exercicios/weather-history_algorithm/wunderground_parser_wl.py)

> ![image](https://user-images.githubusercontent.com/47596121/65840560-04616c00-e2f1-11e9-8743-a27ef4f6899d.png)

>- [`combine_csv_files.py`](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_16/exercicios/weather-history_algorithm/combine_csv_files.py)

>![image](https://user-images.githubusercontent.com/47596121/65841003-72a82d80-e2f5-11e9-8270-a7be4591e7de.png)

- Versão do Google Chrome utilizado com o Selenium: 77.0.3865.90
- Versão do ChromeDriver utilizado: [ChromeDriver 77.0.3865.40](https://chromedriver.storage.googleapis.com/index.html?path=77.0.3865.40/)


# Updated by me from the original
The function wunderground_parser_wl() works fine now with the new web pages with JS from WunderGroud.
However, it is extremely slow because it uses Selenium with ChromeDriver, so
I made sure that it only looks for the wunderground.com pages of the months,
as it is much better to do this with only 12 pages than 365. I advise testing
with every page of each day of the year, try to make sure that it works with
the date you prefer to use.

# Organização do Projeto
```
├── wund_weather_data          <- Contém dados .csv do wunderground.
├── README.md	                <- README bonitinho
├── combine_csv_files.py             <- Execute isso para juntar e pegar os dados.
├── wunderground_parser.py     <- Analisa o .html com dados meteorológicos do wunderground.
├── wunderground_scraper.py    <- Pega o .html do site do wunderground.
```
