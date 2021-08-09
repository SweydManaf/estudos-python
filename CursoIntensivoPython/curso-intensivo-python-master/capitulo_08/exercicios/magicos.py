def mostrar_magicos(magicos: list) -> None:
    """Mostra o nome de cada mágico da lista."""
    for magico in magicos:
        print(magico.title())


nomes = ['william', 'steve', 'bill', 'phill', 'sarah']
mostrar_magicos(nomes)
