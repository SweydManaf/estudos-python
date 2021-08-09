def construir_album(
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


def nome_do_artista(prompt: str = 'Nome do artista: ') -> str:
    """
    -> Pergunta e recebe o nome do artista do álbum.
    :param prompt: Recebe uma string para saber o nome artista.
    :return: Retorna o nome do artista.
    """
    while True:
        nome = str(input(prompt)).split()
        if '-'.join(nome).replace('-', '').isalpha():
            nome = ' '.join(nome)
            return nome
        print('Digite um valor para o nome do artista válido.')


def titulo_do_album(prompt: str = 'Título do álbum: ') -> str:
    """
    -> Pergunta e recebe o título do álbum.
    :param prompt: Recebe uma string para saber o título do álbum.
    :return: Retorna o título do álbum.
    """
    while True:
        titulo = str(input(prompt)).split()
        if '-'.join(titulo).replace('-', '').isalpha():
            titulo = ' '.join(titulo)
            return titulo
        print('Digite um valor para o título do álbum válido.\n')


def numero_de_faixas(
        prompt: str = 'Digite o número de faixas do álbum: ') -> int:
    """
    -> Pergunta e recebe o número de faixas do álbum.
    :param prompt: Recebe uma string para saber o título do álbum.
    :return: Retorna o número de faixas do álbum.
    """
    while True:
        try:
            num_faixas = int(input(prompt))
        except (ValueError, TypeError):
            print('Digite um número inteiro de faixas válido.\n')
        else:
            return num_faixas


def mostrar_album(album: dict) -> None:
    """
    -> Exibe as informações fornecidas
    contidas sobre o álbum do dicionário.
    :param album: Dicionário contendo as informações.
    """
    # Exibe as informações fornecidas do dicionário.
    print('\nINFORMAÇÕES SOBRE O ÁLBUM MUSICAL:')
    for k, v in album.items():
        if k == 'artista':
            print(f'\tNome do artista: {v.title()}')
        if k == 'album':
            print(f'\tTítulo do álbum: {v.title()}')
        if k == 'n_faixas':
            print(f'\tNúmero de faixas: {v}')


def interromper_loop(
        prompt='Deseja construir outro álbum musical?\n[S/N] '):
    """
    -> Verifica se quer interromper o loop while.
    :return: Retorna a resposta da pergunta do prompt.
    """
    while True:
        continuar = str(input(f'\n{prompt}')).upper().strip()
        if continuar.replace(' ', '').isalpha():
            if continuar in 'SN':
                return continuar
        print('Digite apenas "S" ou "N".')


# Programa principal.
while True:
    nome = nome_do_artista('\nDigite o nome do artista: ')
    titulo = titulo_do_album('Digite o título do álbum: ')
    while True:
        prompt = '\nDeseja adicionar o número de faixas do álbum?\n[S/N] '
        resposta = str(input(prompt)).upper().strip()
        if resposta.replace(' ', '').isalpha():
            if resposta in 'SN':
                if resposta == 'S':
                    faixas = numero_de_faixas()
                    # Adiciona o álbum, o artista e o número de faixas
                    # no dicionário.
                    album = construir_album(nome, titulo, faixas)
                else:
                    print('O número de faixas não será adicionado no dicionário.')
                    album = construir_album(nome, titulo)
                break
        print('Digite apenas "S" ou "N".\n')
    mostrar_album(album)
    continuar = interromper_loop()
    if continuar == 'N':
        print('\nFinalizando...')
