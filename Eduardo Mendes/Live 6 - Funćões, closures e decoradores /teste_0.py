"""
1 - Funćões nomeadas (def)
2 - Funcões anonimas (lambda)
3 - Funções de classe (class)
"""

def nomeada_soma(x, y):
    return x + y

anonima_soma = lambda x, y: x + y

class classSoma():
    def __int__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.x + self.y
