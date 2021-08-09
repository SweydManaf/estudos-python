def cidade_pais(cidade: str, pais: str, populacao: int = 0) -> str:
    """
    -> Aceita o nome de uma cidade, o nome
    do país e a população dessa cidade,
    retorna essas informações formatadas.

    :param cidade: Nome da cidade.
    :param pais: Nome do país.
    :param populacao: Número da população da cidade.
    :return: Retorna uma string com o nome da
    cidade, do país e a população a cidade no
    formato 'Cidade, País - população XXX'.
    """
    if populacao:
        nome_formatado = (f'{cidade.title()}, {pais.title()} '
                          f'- população {populacao}')
    else:
        nome_formatado = f'{cidade}, {pais}'.title()

    return nome_formatado
