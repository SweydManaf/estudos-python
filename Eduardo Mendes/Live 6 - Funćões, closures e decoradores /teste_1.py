# Função nomeada
def soma(x, y):
    """
    Função que soma dois valores.
    """
    return x + y

# Função anonima
#print(list(map(lambda x: x + 2, [1,2,3])))
soma_2 = (lambda x: x + 2)
#print(soma_2(2))


# Função como classe
class classSoma:
    def __call__(self, x, y):
        return x + y


print(classSoma()(2, 2))