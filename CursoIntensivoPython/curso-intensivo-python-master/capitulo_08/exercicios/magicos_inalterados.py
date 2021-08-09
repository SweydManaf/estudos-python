def mostrar_magicos(magicos: list) -> None:
    """Mostra o nome de cada mágico da lista."""
    for magico in magicos:
        print(f'\t{magico.title()}')


def grandes_magicos(magicos: list) -> list:
    """Adiciona 'o Grande' no nome de cada mágico da lista."""
    for magico in magicos:
        magico_atual = magico
        grande_magico = f'{magico_atual}, o Grande'
        magicos.insert(magicos.index(magico_atual), grande_magico)
        magicos.remove(magico_atual)

    return magicos


nomes = [
    'william rodrigues',
    'steve jobs',
    'bill wallace',
    'phill lara',
    'sarah connor'
    ]
mostrar_magicos(nomes)

print('\nOs grandes mágicos:')
os_grandes_magicos = grandes_magicos(nomes[:])
mostrar_magicos(os_grandes_magicos)

print('\nLista de nomes original:')
mostrar_magicos(nomes)
