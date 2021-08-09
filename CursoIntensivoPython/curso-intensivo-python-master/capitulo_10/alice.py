filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f'Sorry, the file {filename} does not exist.'
    print(msg)
else:
    # Conta o número aproximado de palavras no arquivo.
    words = contents.split()
    num_words = len(words)

    print(f'The file {filename} has about {num_words}.')
