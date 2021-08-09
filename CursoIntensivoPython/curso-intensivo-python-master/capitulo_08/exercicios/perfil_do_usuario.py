def construir_perfil(p_nome: str, u_nome: str, **info_usuario) -> dict:
    """
    -> Constrói um dicionário contendo tudo que sabemos sobre um usuário.
    :param p_nome: Primeiro nome.
    :param u_nome: Último nome.
    :param info_usuario: Dicionário contendo informações extras.
    :return: Retorna um dicionário contendo informações sobre
    um usuário.
    """
    perfil = dict()
    perfil['first_name'] = p_nome
    perfil['last_name'] = u_nome

    for key, value in info_usuario.items():
        perfil[key] = value

    return perfil


perfil_do_usuario = construir_perfil('william', 'rodrigues',
                                     idade=19, sexo='masculino')
print(perfil_do_usuario)
