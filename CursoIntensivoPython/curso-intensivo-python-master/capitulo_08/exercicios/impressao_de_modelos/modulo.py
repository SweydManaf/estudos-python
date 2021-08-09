def imprima_modelos(
        designs_nao_impressos: list, modelos_completos: list) -> None:
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.
    :param designs_nao_impressos: Lista de designs que ainda vão ser
    impressos.
    :param modelos_completos: Lista de modelos que já foram impressos.
    """
    while designs_nao_impressos:
        design_atual = designs_nao_impressos.pop()
        # Simula a criação de uma impressão 3D a partir do design.
        print(f'Imprimindo modelo: {design_atual}')
        modelos_completos.append(design_atual)


def mostrar_modelos_completos(modelos_completos: list) -> None:
    """
    Mostra todos os modelos impressos.
    :param modelos_completos: Lista de modelos que já foram impressos.
    """
    print(f'\nOs seguintes modelos foram impressos:')
    for modelo_completo in modelos_completos:
        print(f'\t- {modelo_completo}')
