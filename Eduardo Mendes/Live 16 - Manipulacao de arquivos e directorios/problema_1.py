import os.path
import shutil

# Criar path caso ele não exista
if not os.path.exists('aulinha_1'):
    os.mkdir('aulinha_1')

# Entra no diretório
os.chdir('aulinha_1')

# Criar arquivo xpto
with open('xpto.txt', 'w') as f:
    f.write('')

# Copia os arquivos
for element in range(1, 4):
    shutil.copy('xpto.txt', f'xpto_{element}.txt')


# Printa o diretório presente
# print(os.getcwd())

# Faz uma asssertiva se no diretório tem 4 arquivos
assert len(os.listdir('.')) == 4
