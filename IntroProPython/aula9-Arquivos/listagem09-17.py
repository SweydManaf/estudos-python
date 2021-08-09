import os
# Cria um arquivo e o fecha imedatiamente

open('moribundo.txt', 'w').close()
os.mkdir('vago')
os.rmdir('vago')
os.remove('moribundo.txt')
