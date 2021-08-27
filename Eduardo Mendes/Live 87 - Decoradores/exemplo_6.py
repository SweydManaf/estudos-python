"""Decorados com params"""

def validate_type(type):
    # type é livre
    def validade(func):
        # func é livre
        def inner(*args, **kwargs):
            ...
        return inner
    return validade