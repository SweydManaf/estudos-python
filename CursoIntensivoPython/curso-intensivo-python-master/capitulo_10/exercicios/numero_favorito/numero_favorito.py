import json

arquivo = '../arquivos_json/numero_favorito.json'


def obter_numero_armazenado() -> int or None:
    """
    -> Obtém o número favorito do usuário já
    armazenado se estiver disponível.

    :return: Retorna o número favorito armazenado.
    """
    try:
        with open(arquivo) as obj_arq:
            numero = json.load(obj_arq)
    except FileNotFoundError:
        return None
    else:
        return numero


def obter_novo_numero() -> int:
    """
    -> Obtém um novo número favorito do usuário.
    Só aceita números inteiros, se não um erro
    de valor personalizado será mostrado.

    :return: Retorna o novo número favorito digitado pelo usuário.
    """
    try:
        numero = int(input('Qual é o seu número favorito? '))
    except ValueError:
        print('ERRO: digite um número inteiro válido.')
    else:
        with open(arquivo, 'w') as obj_arq:
                json.dump(numero, obj_arq)

        return numero


def mostrar_numero():
    """
    -> Mostra o número favorito do usuário.
    Se o número estiver armazenado, mostra uma
    mensagem dizendo qual é o número. Se não,
    obtém um novo número favorito do usuário.
    """
    numero = obter_numero_armazenado()
    if numero:
        print(f'Eu sei qual é o seu número favorito! É {numero}.')
    else:
        numero = obter_novo_numero()
        if numero:
            print(f'O seu número favorito ({numero}) foi armazenado com sucesso.')


mostrar_numero()
