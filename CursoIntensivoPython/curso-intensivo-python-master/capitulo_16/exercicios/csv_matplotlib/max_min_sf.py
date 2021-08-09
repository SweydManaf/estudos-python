import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from obter_dados_csv import obter_datas_temperaturas


# Nome do arquivo csv com os dados de San Francisco, 2014.
arquivo = 'san_francisco_2014.csv'

# Obtém as datas, temperaturas máximas e mínimas.
dados = obter_datas_temperaturas(arquivo)
datas = dados[0]
maximas = dados[1]
minimas = dados[2]

# Faz a plotagem dos dados.
fig = plt.figure(dpi=128, figsize=(10, 6))

# Formata xaxis com 1 mês de intervalo e o formato da data.
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.plot(datas, maximas, c='red', alpha=0.5)
plt.plot(datas, minimas, c='blue', alpha=0.5)
plt.fill_between(datas, maximas, minimas, facecolor='blue', alpha=0.1)

# Formata o gráfico.
title = 'Daily high and low temperatures - 2014\nSan Francisco, CA'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('imagens/highs_lows_sf.png')
plt.show()
