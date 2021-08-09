def mostrar_magicos(magicos: list) -> None:
    """Mostra o nome de cada mágico da lista."""
    for magico in magicos:
        print(f'\t{magico.title()}')


def grandes_magicos(magicos: list) -> None:
    """Adiciona 'o Grande' no nome de cada mágico da lista."""
    for magico in magicos:
        magico_atual = magico
        grande_magico = f'{magico_atual}, o Grande'
        magicos.insert(magicos.index(magico_atual), grande_magico)
        magicos.remove(magico_atual)


nomes = [
    'william rodrigues',
    'steve jobs',
    'bill wallace',
    'phill lara',
    'sarah connor'
    ]
mostrar_magicos(nomes)

print('\nOs grandes mágicos:')
grandes_magicos(nomes)
mostrar_magicos(nomes)
