def cidade_pais(cidade: str, pais: str) -> str:
    """
    -> Devolve o nome da cidade e do seu país formatados
    de forma elegante.
    :param cidade: O nome da cidade.
    :param pais: O nome do país.
    :return: Retorna a string -> 'Cidade, País'
    """
    return f'{cidade}, {pais}'.title()


cidade_pais_1 = cidade_pais('rio de janeiro', 'brasil')
print(cidade_pais_1)
cidade_pais_2 = cidade_pais('santiago', 'chile')
print(cidade_pais_2)
cidade_pais_3 = cidade_pais('las vegas', 'estados unidos')
print(cidade_pais_3)
