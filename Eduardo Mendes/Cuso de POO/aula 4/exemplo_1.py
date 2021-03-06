class Dois:
    val = 2
    def __neg__(self):
        print('Ola so, negativei')
        return -self.val
    def __pos__(self):
        print('Olha so, positivei')
        return +self.val



class MinhaString:
    def __init__(self):
        self.s = 'Live de python'

    def __neg__(self):
        return self.s[::-1]


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Ponto(-self.x, -self.y)

    def __pos__(self):
        return Ponto(+self.x, +self.y)

    def __repr__(self):
        """Respresenta a classe"""
        return f'Ponto({self.x}, {self.y})'
