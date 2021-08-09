def fazer_sanduiche(*ingredientes):
    """
    -> Apresenta um resumo do sanduíche que foi pedido.
    :param ingredientes: Ingredientes que a pessoa quer no sanduíche.
    """
    print('\nO sanduíche ficará pronto com os seguintes ingredientes:')
    for ingrediente in ingredientes:
        print(f'\t- {ingrediente}')


fazer_sanduiche('frango desfiado', 'pão de forma')
fazer_sanduiche('pão de forma integral')
fazer_sanduiche('peito de frango', 'tempero verde', 'cebola')
