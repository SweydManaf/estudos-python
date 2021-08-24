import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

# Faz uma chamada de API e armazena a resposta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Processa informações sobre cada artigo submetido
submission_ids = r.json()
submission_dicts = []
active_site = 0
for submission_id in submission_ids[:30]:
    # Cria uma chamada de API separada para cada artigo submetido

    url = f'https://hacker-news.firebaseio.com/v0/item/{str(submission_id)}.json'
    submission_r = requests.get(url)
    if submission_r.status_code == 200:
        active_site += 1
        print(f'Processing {active_site} of 30')
    else:
        print(f'Problem with this id: {submission_id}')
        print('\033[31mYour graph will probably have an error\033[m')
    response_dict = submission_r.json()

    # Armazena dados sobre o artigo
    submission_dict = {
        'title': response_dict['title'],
        'link': f'http://news.ycombinator.com/item?id={str(submission_id)}',
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

# Organiza iniciando do mais top
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Obtem dados para a visualização grafica
plot_dicts = []
for submission_dict in submission_dicts:
    plot_dict = {
        'value': submission_dict['comments'],
        'xlink': submission_dict['link']
    }
    plot_dicts.append(plot_dict)


# Cria uma visualização
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45

my_config.show_y_guides = True
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Discussion'
chart.x_labels = [submission_dict['title'] for submission_dict in submission_dicts]

chart.add('', plot_dicts)
chart.render_to_file('hn_discussion.svg')
print('Your graph is complete.')
