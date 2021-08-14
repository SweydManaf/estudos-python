"""Funćões como objeto de primeira classe."""

from typing import Callable, Dict
from numbers import Number

func = lambda: 'resulaltado da funćão'

calc: Dict[str, Callable] = {
    'soma': lambda x, y: x + y,
    'subtração': lambda x, y: x - y,
    'multiplicacao': lambda x, y: x * y,
    'divisao': lambda x, y: x / y
}


def soma(x: Number, y: Number) -> Number:
    """Soma dois números."""
    return x + y


def sub(x: Number, y: Number) -> Number:
    """Subtrai dois números."""
    return x - y


def mult(x: Number, y: Number) -> Number:
    """Multiplica dois números."""
    return x * y


def div(x: Number, y: Number) -> Number:
    """Divide dois números."""
    return x / y


calc_nomeado = {
    'soma': soma,
    'subtração': sub,
    'multiplicacao': mult,
    'divisao': div
}

somas = [lambda x: x + 0,
         lambda x: x + 1,
         lambda x: x + 2
         ]
print(somas[2](5))
