def camiseta(tamanho: str, mensagem: str):
    """
    -> Faz uma camiseta, baseando-se no tamanho e
    na mensagem da estampa.
    :param tamanho: Tamanho da camiseta.
    :param mensagem: Mensagem que será estampada na camiseta.
    """
    print(f'\nA camiseta terá o tamanho {tamanho.upper()}, e a mensagem da estampa:'
          f'\n\t"{mensagem.upper()}"')


# Usando argumentos posicionais.
camiseta('m', 'kiss me hard before you go')
# Usando argumentos nomeados.
camiseta(mensagem='nerd power', tamanho='g')
