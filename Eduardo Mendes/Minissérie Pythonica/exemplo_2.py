"""Serie de funćões # 2"""

anonima = lambda param : param + 2
anonima_plus = lambda param1, param2 : param1 + param2

def soma_posicional(x,y):
    """
    :param x e y: paramatro posicional
    :return:
    """
    return x + y

def soma_nomeados(x=7, y=7):
    """
    :param x e y: parametros nomeados
    :return: na falta de x ou y , o valor 7 será usado
    """
    print(f'x: {x}, y: {y}')
    return x + y

def soma_explicitamente_nomeados(*, x=7, y=7):
    """
    :param x e y: parametros nomeados
    :return: na falta de x ou y , o valor 7 será usado
    """
    print(f'x: {x}, y: {y}')
    return x + y


def soma_explicitamente_posicionais(x, y , /):
    """
    :param x e y: parametros nomeados
    :return: na falta de x ou y , o valor 7 será usado
    """
    print(f'x: {x}, y: {y}')
    return x + y

def soma_tudo_mix(x, y, /, z, *, w):
    return sum((x, y, z, w))

print(soma_tudo_mix(1,2,3,w=1))
