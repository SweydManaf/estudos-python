import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
from datetime import datetime

# Obtem os indices pluviometricos
filename = open('fortaleza_rainfall_2018.csv')
with filename as f:
    reader = csv.reader(f)
    next(reader)

    dates, indices_pluvio = [], []
    for linha in reader:
        try:
            date = datetime.strptime(linha[0], '%Y-%m-%d').date()
            indice_pluvio = float(linha[16])
        except ValueError:
            print(f'{linha[0]} - Faltando dados...')
        else:
            dates.append(date)
            indices_pluvio.append(indice_pluvio)



# Plota os dados no grafico
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, indices_pluvio)

# Formata a data dos dados
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# Formata os dados no grafico
plt.title('Indice Pluviometrico\n Fortaleza, CE')
plt.ylabel('Indice pluviometrico')
plt.xlabel('')
fig.autofmt_xdate()
plt.show()
