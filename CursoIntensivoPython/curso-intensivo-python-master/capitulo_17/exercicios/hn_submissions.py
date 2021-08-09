import requests

import pygal
from pygal.style import NeonStyle as NS, LightenStyle as LS

from operator import itemgetter


# Faz uma chamada de API e armazena a resposta.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Processa informações sobre cada artigo submetido.
submissions_ids = r.json()

submission_dicts = []
for submission_id in submissions_ids[:30]:
    # Cria uma chamada de API separada para cada artigo submetido.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    submission_r = requests.get(url)
    print(submission_r.status_code)
    
    response_dict = submission_r.json()
    submission_dict = {
        'title': response_dict['title'],
        'link': f'http://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, 
                          key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

titles, plot_dicts = [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    plot_dict = {
        'value': submission_dict['comments'],
        'label': submission_dict['title'],
        'xlink': submission_dict['link'],
    }
    plot_dicts.append(plot_dict)

# Cria uma visualização.
my_style = LS('#333366', base_style=NS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
my_config.y_title = 'Number of Comments'

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Active Discussions on Hacker News'
chart.x_labels = titles

chart.add('', plot_dicts)
chart.render_to_file('imagens/hg_discussions.svg')
