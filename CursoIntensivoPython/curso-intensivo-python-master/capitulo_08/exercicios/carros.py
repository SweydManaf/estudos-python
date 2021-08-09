def info_carro(fabricante: str, modelo: str, **info_extra) -> dict:
    """
    -> Guarda as informações de um imagem em um dicionário.
    :param fabricante: Nome do fabricante do imagem.
    :param modelo: Nome do modelo do imagem.
    :param info_extra: Dicionário contendo informações extras do imagem.
    :return: Retorna um dicionário contendo informações sobre o imagem.
    """
    carro = dict()
    carro['fabricante'] = fabricante
    carro['modelo'] = modelo

    for k, v in info_extra.items():
        carro[k] = v

    return carro


carro_dict = info_carro('subaru', 'outback',
                        cor='azul', reboque=True)
print(carro_dict)
