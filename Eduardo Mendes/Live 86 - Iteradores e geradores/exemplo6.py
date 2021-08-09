def raio_simplificado(lista_composta):
    for elemento in lista_composta:
        yield from elemento


lista_composta = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

