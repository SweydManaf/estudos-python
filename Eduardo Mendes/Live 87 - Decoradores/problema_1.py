def validate_type(type, *args):
    return all(isinstance(val, int) for val in args)

def soma(x, y):
    '''Função qe soma qualquer coisa.'''
    if all(isinstance(val, int) for val in [x, y]):
        return x + y

def sub(x, y):
    if all(isinstance(val, int) for val in [x, y]):
        return x - y