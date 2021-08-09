class Employee:
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenonme = sobrenome
        self.salario = salario

    def giv_raise(self, aumento=5000):
        self.salario += aumento

