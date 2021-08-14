"""Anotaćões de tipo PEP-484"""

from numbers import Number
from typing import List, Dict, Union


# issubclass(int, Number)
def soma(x: Number, y: Number) -> Number:
    return x + y


def cadastro_usuario(
        nome: str,
        idade: int,
        gostos: List[str]) -> Dict[str, Union[str, int, List[str]]]:
    return {
        nome: nome,
        idade: idade,
        gostos: gostos
    }


print(cadastro_usuario('eduardo', 26, ['ouvir musica', 'Python']))

# NÃO ENTENDI
