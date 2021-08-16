"""High order fuctions"""


from typing import Callable, Any


soma_2 = lambda val: val + 2

# Twice
def reaplica(func: Callable, val: Any) -> Any:
    """Função que reaplica a funćão a funćão ao resultado da chamada"""
    return func(func(val))


def seleciona(op: str) -> Callable:
    """Seleciona uma funcao usando seu nome"""
    ops = {
        'soma': lambda x, y: x + y,
        'sub': lambda x, y: x - y
    }
    return ops[op]

print(seleciona('soma')(1,2))

def teke_cond(func, valores):
    for val in valores:
        if func(val):
            yield val
        else:
            break

# NÃO ENTENDI