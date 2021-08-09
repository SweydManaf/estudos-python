def descreva_cidade(cidade: str, pais: str) -> None:
    """
    -> Exibe uma mensagem simples dizendo em que país
    está localizada a cidade.
    :param cidade: Nome da cidade.
    :param pais: Nome do país.
    """
    print(f'{cidade.title()} está localizado(a) no(a) {pais.title()}.')


# Usando argumentos posicionais.
descreva_cidade('reykjavik', 'islândia')
descreva_cidade('rio de janeiro', 'brasil')
# Usando argumentos nomeados.
descreva_cidade(pais='islândia', cidade='reykjavik')
descreva_cidade(pais='brasil', cidade='rio de janeiro')
