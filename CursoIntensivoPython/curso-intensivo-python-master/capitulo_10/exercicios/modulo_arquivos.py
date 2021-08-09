def obter_data_horario() -> str:
    """
    -> Pega a data e o horário do sistema, essa função
    será utilizada em outras funções para informações
    mais precisas que necessitem dessas opções.

    Obs: O retorno da data e do horário é dado quando
    essa função é executada, seja por outra função ou não.

    :return: Retorna uma string com a data e o horário
    atuais do sistema, a partir do momento em que a
    função foi usada.
    """
    from datetime import datetime

    # Pega a data e o horário de agora.
    agora = datetime.now()

    return agora.strftime('%d/%m/%Y, %H:%M:%S')


def escrever_info_enquete(arquivo: str, nome: str, resposta: str):
    """
    -> Escreve e concatena uma linha com informações de uma
    enquete feita sobre programação.
    Essas informações são: o nome do entrevistado, a resposta
    do mesmo, a data e o horário em que a pessoa deu a resposta.

    Avisos: Se o arquivo não existir no mesmo repositório que essa
    função estiver sendo usada, um arquivo com a string fornecida
    será gerado no mesmo repositório.
    Se o path do arquivo fornecido estiver incorreto, um erro
    personalizado será informado.

    Obs: Essa função não sobrescreve o conteúdo de um arquivo existente,
    pelo contrário, ela adiciona uma linha no final do arquivo.

    :param arquivo: String com o nome/path do arquivo.
    :param nome: Nome do entrevistado.
    :param resposta: Resposta dada pelo entrevistado.
    """
    data_horario = obter_data_horario()
    try:
        with open(arquivo, 'a') as obj_arq:
            obj_arq.write(f'{nome.title()}, {resposta.capitalize()}., '
                          f'{data_horario}\n')
    except FileNotFoundError:
        print(f"\nDesculpe, o arquivo '{arquivo}' não existe.")
    else:
        print(f'\n\t{nome}, muito obrigado por responder nossa enquete!')


def escrever_nome_dos_convidados(arquivo: str, convidado: str):
    """
    -> Escreve e concatena uma linha com o nome do convidado e
    com a data e o horário formatados em que o convidado foi
    adicionado no arquivo com a lista de convidados.

    Avisos: Se o arquivo não existir no mesmo repositório que essa
    função estiver sendo usada, um arquivo com a string fornecida
    será gerado no mesmo repositório.
    Se o path do arquivo fornecido estiver incorreto, um erro
    personalizado será informado.

    Obs: Diferente da função escrever_nome_do_convidado(), essa
    função não sobrescreve o conteúdo de um arquivo existente,
    pelo contrário, ela adiciona uma linha no final do arquivo.

    :param arquivo: String com o nome/path do arquivo.
    :param convidado: Nome do convidado.
    """
    data_horario = obter_data_horario()
    try:
        with open(arquivo, 'a') as obj_arq:
            obj_arq.write(f'{data_horario} -> {convidado.title()}\n')
    except FileNotFoundError:
        print(f"Desculpe, o arquivo '{arquivo}' não existe.")


def escrever_nome_do_convidado(arquivo: str, convidado: str):
    """
    -> Escreve o nome do convidado em uma linha de um arquivo
    existente.

    Avisos: Se o arquivo não existir no mesmo repositório que essa
    função estiver sendo usada, um arquivo com a string fornecida
    será gerado no mesmo repositório.
    Se o path do arquivo fornecido estiver incorreto, um erro
    personalizado será informado.

    Cuidado: Essa função sobrescreve o conteúdo de um arquivo
    já existente, certifique-se de que o conteúdo do arquivo
    não seja importante.

    :param arquivo: String com o nome/path do arquivo.
    :param convidado: Nome do convidado.
    """
    try:
        with open(arquivo, 'w') as obj_arq:
            obj_arq.write(convidado.title())
    except FileNotFoundError:
        print(f"Desculpe, o arquivo '{arquivo}' não existe.")


def escrever_mensagem(arquivo: str, msg: str):
    """
    -> Escreve e concatena uma linha com a mensagem do exercício
    no final de um arquivo existente.

    Avisos: Se o arquivo não existir no mesmo repositório que essa
    função estiver sendo usada, um arquivo com a string fornecida
    será gerado no mesmo repositório.
    Se o path do arquivo fornecido estiver incorreto, um erro
    personalizado será informado.

    :param arquivo: String com o nome/path do arquivo.
    :param msg: String pra a mensagem que será escrita no arquivo.
    """
    try:
        with open(arquivo, 'a') as obj_arq:
            obj_arq.write(f'Em Python podemos... {msg.capitalize()}.\n')
    except FileNotFoundError:
        print(f"Desculpe, o arquivo '{arquivo}' não existe.")


def ler_arquivo_inteiro(arquivo: str) -> str:
    """
    -> Lê o arquivo inteiro de uma vez usando a função read().

    Aviso: Se o path do arquivo fornecido estiver incorreto,
    um erro personalizado será informado.

    :param arquivo: String com o nome/path do arquivo.
    :return: Retorna o conteúdo do arquivo.
    """
    try:
        with open(arquivo) as obj_arq:
            conteudo = obj_arq.read()
    except FileNotFoundError:
        return f"Desculpe, o arquivo '{arquivo}' não existe."
    else:
        return conteudo


def ler_arquivo_diretamente(arquivo: str) -> list or None:
    """
    -> Utiliza um laço for no objeto arquivo para ler
    linha por linha do arquivo.
    Adiciona cada linha em uma lista com todas as linhas.

    Aviso: Se o path do arquivo fornecido estiver incorreto,
    nenhuma mensagem de erro será mostrada e um NoneType objeto
    será retornado.
    Sendo assim, tente verificar o path do arquivo se isso vier
    a acontecer.

    :param arquivo: String com o nome/path do arquivo.
    :return: Retorna uma lista com todas as linhas do arquivo.
    """
    linhas = []
    try:
        with open(arquivo) as obj_arq:
            for linha in obj_arq:
                linhas.append(linha.rstrip())
    except FileNotFoundError:
        return None
    else:
        return linhas


def ler_arquivo(arquivo: str) -> list or None:
    """
    -> Lê o arquivo linha por linha utilizando a função
    readlines() e armazena em uma lista com todas as linhas.

    Aviso: Se o path do arquivo fornecido estiver incorreto,
    nenhuma mensagem de erro será mostrada e um NoneType objeto
    será retornado.
    Sendo assim, tente verificar o path do arquivo se isso vier
    a acontecer.

    :param arquivo: String com o nome/path do arquivo.
    :return: Retorna uma lista com todas as linhas do arquivo.
    """
    try:
        with open(arquivo) as obj_arq:
            linhas = obj_arq.readlines()
    except FileNotFoundError:
        return None
    else:
        return linhas


def mostrar_arquivo(arquivo: str, modo: int = 1):
    """
    -> Mostra o conteúdo do arquivo de três modos diferentes.
    Se o número do modo não for reconhecido mostra um erro.
    Se o número do modo não for fornecido, mostra o conteúdo
    utilizando o MODO 1.

    Modo 1 (Padrão): Utiliza a função ler_arquivo_indiretamente()
    e mostra o conteúdo de forma simples utilizando um laço for
    retirando a quebra de linha de cada linha.

    Modo 2: Utiliza a função ler_arquivo_diretamente() e mostra
    o conteúdo de forma simples utilizando um laço for, a diferença
    desse para o modo 1 é que não precisa do rstrip() para retirar a
    quebra de linha.

    Modo 3: Utiliza a função ler_arquivo_inteiro() e assim como o
    nome da função diz, mostra o conteúdo inteiro do arquivo do jeito
    que ele estiver, de forma simples.

    Aviso: Se o path do arquivo fornecido estiver incorreto,
    uma mensagem de erro será mostrada, sendo assim, tente
    verificar o path do arquivo se isso vier a acontecer.

    :param arquivo: String com o nome/path do arquivo.
    :param modo: Número do modo que o arquivo será lido.
    :return: Retorna o objeto arquivo lido.
    """
    if modo in [1, 2, 3]:
        if modo == 1:
            linhas = ler_arquivo(arquivo)
            if linhas:
                for linha in linhas:
                    print(linha.rstrip())
            else:
                print(f"Desculpe, o arquivo '{arquivo}' não existe.")
        elif modo == 2:
            linhas = ler_arquivo_diretamente(arquivo)
            if linhas:
                for linha in linhas:
                    print(linha)
            else:
                print(f"Desculpe, o arquivo '{arquivo}' não existe.")
        else:
            conteudo = ler_arquivo_inteiro(arquivo)
            print(conteudo)
    else:
        print('ERRO: digite apenas 1, 2 ou 3 para o '
              'modo que o arquivo será lido.')


def contador_de_palavras(arquivo: str, palavra: str):
    """
    -> Conta a quantidade de ocorrências de uma determinada
    palavra em um arquivo.
    Utiliza a função ler_arquivo_diretamente() para ler o
    arquivo, a quebra de linha é ignorada nesse caso pois
    a função já retira.

    Aviso: Se o path do arquivo fornecido estiver incorreto,
    um erro personalizado será informado.

    Obs: O parâmetro palavra também aceita números, inteiros
    ou floats.

    :param arquivo: String com o nome/path do arquivo.
    :param palavra: Palavra que será contada.
    """
    linhas = ler_arquivo_diretamente(arquivo)
    total = 0
    if linhas:
        for linha in linhas:
            num_palavras = linha.lower().count(str(palavra).lower())
            total += num_palavras

        print(f"O arquivo '{arquivo}' possui {total} "
              f"palavras '{str(palavra).upper()}'.")
    else:
        print(f"Desculpe, o arquivo '{arquivo}' não existe.")
