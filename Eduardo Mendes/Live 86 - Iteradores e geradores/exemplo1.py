def gen_exemplo():
    print('Entrei na funcao')
    yield 'Primeiro'
    print('Estou na funcao')
    yield 'Segundo'
    print('Estou na funcao p.2')
    yield 'Ultimo'
    print('Sai da funcao')

