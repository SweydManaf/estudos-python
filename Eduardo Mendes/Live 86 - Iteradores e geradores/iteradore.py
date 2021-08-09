class MeuIterador:
    def __init__(self):
        self.l = [1,2,3]
        self.index = 0

    def __iter__(self):
        return self # <- retorna o ob. que tem o __next__

    def __next__(self):
        """Explica como pegar o proximo elemento."""
        try:
            proximo = self.l[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration()
        return proximo

teste = MeuIterador()
print(teste.__next__())
print(teste.__next__())
print(teste.__next__())
print(teste.__next__())