def album(
        nome_artista: str, titulo_album: str, n_faixas: int = 0) -> dict:
    """
    -> Constrói um dicionário descrevendo um álbum musical
    contendo o nome do artista, o título do álbum e se fornecido,
    o número de faixas do álbum.
    :param nome_artista: O nome do artista.
    :param titulo_album: O título do álbum.
    :param n_faixas: (Opcional) O número de faixas do álbum.
    :return: Retorna um dicionário que contém o nome do artista,
    o título do álbum e se fornecido, o número de faixas como valores.
    """
    album_musical = {'artista': nome_artista, 'album': titulo_album}
    if n_faixas:
        album_musical['n_faixas'] = n_faixas

    return album_musical


album_1 = album('slipknot', 'iowa')
print(album_1)
album_2 = album('flobots', 'fight with tools')
print(album_2)
album_3 = album('alt-j', 'this is all yours')
print(album_3)
album_4 = album('gorillaz', 'demon days', 15)
print(album_4)
