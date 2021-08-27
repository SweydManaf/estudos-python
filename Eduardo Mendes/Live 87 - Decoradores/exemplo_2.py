def decorador(func):
    def interna(*args, **kwargs):
        print('antes de executar a funcao')
        func(*args, **kwargs)
        print('depois de executar a funcao')

    return interna

@decorador
def ola_bb():
    print('Dentro da funcao')


ola_bb()