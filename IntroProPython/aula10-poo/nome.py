from functools import total_ordering

@total_ordering  # responsavel por implementar todos metodos de comparacao
class Nome:
    def __init__(self, nome):
        self.nome = nome  # 1

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>'\
            .format(id(self), self.__nome, self.__chave, type(self).__name__) #2

    def __eq__(self, outro):
        print('__eq__ Chamado')
        return self.nome == outro.nome

    def __lt__(self, outro):
        print('__lt__ Chamado')
        return self.nome < outro.nome

    @property  # - transorma o metodo em propriedade (read)
    def nome(self):
        return self.__nome

    @nome.setter  # - metodo para definicao de valores (write)
    def nome(self, valor):
        if valor == None or not valor.strip():
            raise ValueError('Nome nao pode ser nulo nem em branco')
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)

    @property
    def chave(self):
        return self.__chave

    @staticmethod  #permite chamar o metodo mesmo sem instancia
    def CriaChave(nome):
        return nome.strip().lower()
