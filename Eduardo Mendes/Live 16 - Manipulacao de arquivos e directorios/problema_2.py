import os
import os.path
import shutil
from pathlib import Path
import re

# Criando arquivos live_n.txt
for el in range(1, 11):
    Path(f'live_{el}.txt').touch()

# List comprehension
l = [f for f in os.listdir('.') if f.startswith('live_')]

# Removendo live_n.txt menor ou igual a 5
for _file in l:
    if int(re.search('\d+', _file).group()) <= 5:
        os.remove(_file)

# List comprehension
l = [f for f in os.listdir('.') if f.startswith('live_')]

# Alterando os arquivos restantes
for val, el in enumerate(sorted(l), 1):
    shutil.move(el, re.sub('\d+', f'{val}', el))
