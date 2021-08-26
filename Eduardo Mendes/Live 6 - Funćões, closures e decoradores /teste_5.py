def decorador(argumentos_decorador):
    '''
    Parametros do decorador
    '''
    print(argumentos_decorador)
    def decorador_real(func):
        '''
        Receber a funcao
        '''
        print(func.__name__)
        def execute_function(*  argumentos_funcao):
            '''
            Executar a funcao
            '''
            print(argumentos_funcao)
        return execute_function
    return decorador_real


@decorador('Anderson')
def soma(x, y):
    return x + y

soma(2, 2)