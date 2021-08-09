#Nilo soluction

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adiciona_cidades(self, cidade):
        cidade.estado = self
        self.cidades.append(cidade)

    def populacao(self):
        return sum([c.populacao for c in self.cidades])

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        self.estado = None
    
    def __str__(self):
        return f'''Cidade (nome={self.nome}, populacao={self.populacao},
    estado={self.estado})'''

# Populacoes obtidas no site da wikipedia
# IBGE estimativa 2012

am = Estado('Amazonas', 'AM')
am.adiciona_cidades(Cidade('manaus', 1861838))
am.adiciona_cidades(Cidade('Parintins', 103828))
am.adiciona_cidades(Cidade('Itacoatiara', 89064))

for estado in [am]:
    print(f'Estado: {estado.nome} Sigla: {estado.sigla}')
    for cidade in estado.cidades:
        print(f'Cidade: {cidade.nome}, Populacao: {cidade.populacao}')
    print(f'Populacaodo Estado: {estado.populacao()}\n')