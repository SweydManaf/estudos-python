def validade_int(func):

    # func é uma variável livre
    def validate(x, y):
        print(x, y)
        return func(x, y)
    return validate


def soma(x, y):
    return x + y

soma_com_validacao = validade_int(soma)

soma_com_validacao(1, 2)