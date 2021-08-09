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
title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

# plt.savefig('imagens/highs_lows_dv.png')
plt.show()
