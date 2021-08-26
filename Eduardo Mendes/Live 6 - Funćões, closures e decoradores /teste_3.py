"""
Closure
"""

from pdb import set_trace

# Ola, Ahoy, hello

def externa(idioma):
    dic = {'pt': 'Olá', 'pi': 'Ahoy', 'en': 'hello'}
    def interna(nome):
        print(f'{dic[idioma]} {nome}')

    return interna

func = externa('pt')
func('Pedro')
func('Sweyd')
func('Eduardo')

func = externa('pi')
func('Pedro')
func('Sweyd')
func('Eduardo')