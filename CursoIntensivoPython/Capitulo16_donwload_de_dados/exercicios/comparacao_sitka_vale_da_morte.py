import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates


def get_datas_weather(filename):
    """Obtem as temperaturas maximas e minimas."""
    with filename as f:
        reader = csv.reader(f)
        next(reader)

        dates, highs, lows = [], [], []
        for linha in reader:
            try:
                date = datetime.strptime(linha[0], '%Y-%m-%d').date()
                high = int(linha[1])
                low = int(linha[3])
            except ValueError:
                print(f'{linha[0]} Missing data')
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)
        return dates, highs, lows


# Obtem as temperaturas maximas e minimas da Sitka
filename_1 = open('sitka_weather_2014.csv')
datas_1 = get_datas_weather(filename_1)
dates_1 = datas_1[0]
highs_1 = datas_1[1]
lows_1 = datas_1[2]

# Obtem as temperaturas maximas e minimas do Vale da morte
filename_2 = open('death_valley_2014.csv')
datas_2 = get_datas_weather(filename_2)
dates_2 = datas_2[0]
highs_2 = datas_2[1]
lows_2 = datas_2[2]

# Plota os dados de Sitka no grafico
fig = plt.figure(figsize=(10, 6), dpi=128)
plt.plot(dates_1, highs_1, c='red')
plt.plot(dates_1, lows_1, c='blue')
plt.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.1)

# Plota os dados do Vale da morte no grafico
plt.plot(dates_2, highs_2, c='red', alpha=0.25)
plt.plot(dates_2, lows_2, c='blue', alpha=0.25)
plt.fill_between(dates_2, highs_2, lows_2, facecolor='blue', alpha=0.25)

# Formata as datas
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# Formatando os dados no grafico
plt.title("Temperaturas maximas e minimas diarias - 2014\n"
          "Vale da Morte e Sitka", fontsize=18)
plt.ylabel("Temperaturas (F)", fontsize=12)
plt.ylim(10, 120)
fig.autofmt_xdate()

plt.show()
