import modulo_arquivos as ma

arquivos = [
    'arquivos_de_texto/livros/alice.txt',
    'arquivos_de_texto/livros/little_women.txt',
    'arquivos_de_texto/livros/moby_dick.txt',
    'arquivos_de_texto/livros/siddhartha.txt',
    ]
for arquivo in arquivos:
    ma.contador_de_palavras(arquivo, 'the')
