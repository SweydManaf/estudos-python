def valida_int(func):
    def interna(*args):
        if all(isinstance(val, int) for val in args):
            return func(*args)
        else:
            return 'Não deu bom.'
    return interna


@valida_int
def soma(x, y):
    return x + y

print(soma('', ''))