import os.path
from pathlib import Path

# Criando pastas não existentes
for x in range(1, 11):
    if not os.path.exists(f'pasta_{x}'):
        os.mkdir(f'pasta_{x}')

l = [path for path in os.listdir('.') if path.startswith('pasta_')]

for path in l:
    Path(os.path.join(path, 'arquivo_1.txt')).touch()
    Path(os.path.join(path, 'arquivo_2.txt')).touch()

for val in sorted(os.walk('.')):
    print(val)