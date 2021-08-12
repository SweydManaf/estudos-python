"""Des|empacomatamneto de argumetos."""


# def meu_sum(**args, **kwargs):
def meu_sum(*grupo_posicioal, **grupo_nomeado):
    """Empacomatamneto"""
    print(grupo_posicioal)
    print(grupo_nomeado)
    print(type(grupo_posicioal))
    print(type(grupo_nomeado))
    return grupo_posicioal, grupo_nomeado


lista = [-1, 1, 2, 3, -3]


def meu_mim(a, b, c, d, *args):
    """Meu min de lista"""
    return min((a, b, c, d, *args))


dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}


def meu_max(a=0, b=0, c=0, d=0):
    """Meu max de dicionario"""
    return max((a, b, c, d))


l = [1, 2, 3]
d = {'d': 4, 'e': 5}


def meu_mix(a, b, c, d=0, e=0):
    """Desemapotamento mixado"""
    return a, b, c, d, e


print(meu_mix(*l, **d))
