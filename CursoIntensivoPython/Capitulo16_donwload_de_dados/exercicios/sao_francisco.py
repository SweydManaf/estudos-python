import csv
import matplotlib.pyplot as plt
from datetime import datetime


# Obtem as temperaturas maximas e minimas
filename = open('san_francisco_2014.csv')
with filename as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, maximas, minimas = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        maxima = int(row[1])
        minima = int(row[3])

        maximas.append(maxima)
        minimas.append(minima)
        dates.append(current_date)

# Plota os dados para analise
fig = plt.figure(dpi=100, figsize=(10, 6))
plt.plot(dates, maximas, c='blue')
plt.plot(dates, minimas, c='blue')
plt.fill_between(dates, maximas, minimas, facecolor='blue', alpha=0.1)

# Formata o grafico
plt.title('Sao Francisco')
plt.ylabel("Temperaturas em F")
fig.autofmt_xdate()
plt.show()
