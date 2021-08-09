def camiseta(
        mensagem: str = 'eu amo python', tamanho: str = 'g') -> None:
    """
    -> Faz uma camiseta, baseando-se no tamanho e
    na mensagem da estampa.
    :param tamanho: Tamanho da camiseta.
    :param mensagem: Mensagem que será estampada na camiseta.
    """
    print(f'\nA camiseta terá o tamanho {tamanho.upper()}, e a mensagem da estampa:'
          f'\n\t"{mensagem.upper()}"')


# Usando argumentos posicionais.
camiseta()
camiseta('python é amor', 'p')
# Usando argumentos nomeados.
camiseta(tamanho='m')
camiseta(mensagem='python é amor', tamanho='p')
