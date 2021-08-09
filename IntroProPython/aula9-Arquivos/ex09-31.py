import os.path
if os.path.exists('a'):
    print('O a existe.')
    if os.path.isdir('a'):
        print('E e um diretorio.')
    else:
        print('Mas nao e um diretorio e sim um arquivo. ')
else:
    print('O diretorio a nao existe')