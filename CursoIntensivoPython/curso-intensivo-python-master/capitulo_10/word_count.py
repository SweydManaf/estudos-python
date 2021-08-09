def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Conta o número aproximado de palavras no arquivo.
        words = contents.split()
        num_words = len(words)

        print(f'The file {filename} has about {num_words}.')


filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
