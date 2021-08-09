# Referências Rápidas do Capítulo

- ### Utilização do [_Pygal_](pygal.org) para gerar gráficos baseado em dados online
Usando a [API do GitHub](https://developer.github.com/v3/) para verificar os principais repositórios do Python baseados na maior quantidade
de estrelas de agora (2019/10) e gerar uma visualzação contendo o nome do repositório, com uma descrição na barra de cada um e com o link
direto para o mesmo na barra clicável. [Aqui](https://github.com/willy-r/curso-intensivo-python/tree/master/capitulo_17/exercicios/imagens) tem de outras linguagens.
>- [_python_repos.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_17/exercicios/language_repos.py)

```
import requests

import pygal
from pygal.style import NeonStyle as NS, LightenStyle as LS


# Faz uma chamada de API e armazena a resposta.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Armazena a resposta da API em uma variável.
response_dict = r.json()
print(f'Total repositories: {response_dict["total_count"]}')

# Explora informações sobre os repositórios.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Pega a descrição do projeto, se estiver disponível.
    description = repo_dict['description']
    if not description:
        description = 'No description provided.'

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
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

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('imagens/python_repos.svg')
```

<img src='https://user-images.githubusercontent.com/47596121/66003909-c180cf00-e47d-11e9-8c3a-1a18a63eb844.png' heigth='830' width='700'>

> [_NeonStyle_](http://pygal.org/en/stable/documentation/builtin_styles.html#neon) do Pygal.

---

Usando a parte [`topstories`](https://hacker-news.firebaseio.com/v0/topstories.json) da API do site Hacker News para pegar os principais
tópicos baseados na maior quantidade comentários e gerar uma visualização com o nome do tópico, o número de comentários e a barra clicável com o link do mesmo.
>- [_hn_submissions.py_](https://github.com/willy-r/curso-intensivo-python/blob/master/capitulo_17/exercicios/hn_submissions.py)

```
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
```

<img src='https://user-images.githubusercontent.com/47596121/66004679-c0e93800-e47f-11e9-8348-6941872c226d.png' heigth='830' width='700'>

> [_NeonStyle_](http://pygal.org/en/stable/documentation/builtin_styles.html#neon) do Pygal.

---
