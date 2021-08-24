import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def callAPI(language):
    """Faz a chamada da API  e retorna a resposta."""
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
    r = requests.get(url)
    return r


def getData(response):
    """Obtem e retorna os dados e armazena em um dicionario."""
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts


def getDataToPlot(repo_dicts):
    """Processa os dados e os organiza para a plotagem de dados"""
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        # Adiciona uma descrićão para os repositorios que não tem
        if not repo_dict['description']:
            repo_dict['description'] = 'No description provided.'

        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url']
        }
        plot_dicts.append(plot_dict)
    return names, plot_dicts


def makeVisualization(names, plot_dicts):
    my_style = LS('#333366', base_style=LCS)

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred JavaScript Projects on GitHub'
    chart.x_labels = names
    chart.add('', plot_dicts)

    chart.render_to_file('javascript_repos.svg')


r = callAPI('javascript')
repo_dicts = getData(r)
names, plot_dicts = getDataToPlot(repo_dicts)
makeVisualization(names, plot_dicts)
