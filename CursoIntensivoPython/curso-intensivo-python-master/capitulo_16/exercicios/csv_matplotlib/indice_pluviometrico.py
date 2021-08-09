import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from obter_dados_csv import obter_datas_indices_pluvio


# Nome do arquivo csv com os dados do Ceará, 2018.
arquivo = 'fortaleza_rainfall_2018.csv'

# Obtém as datas e os indices pluviométricos.
dados = obter_datas_indices_pluvio(arquivo)
datas = dados[0]
indices_pluvio = dados[1]

# Plota os dados.
fig = plt.figure(dpi=128, figsize=(10, 6))

# Formata xaxis com 1 mês de intervalo e o formato da data.
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.plot(datas, indices_pluvio, c='blue', alpha=0.5)
plt.fill_between(datas, indices_pluvio, facecolor='blue', alpha=0.2)

# Formata o gráfico.
title = "Daily rainfall amounts - 2018\nFortaleza, CE"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('imagens/rainfall_fortaleza.png')
plt.show()
