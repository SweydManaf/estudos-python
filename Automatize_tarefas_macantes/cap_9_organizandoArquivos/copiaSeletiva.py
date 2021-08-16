import os
import shutil
import re

# Correspondecia para arquivos png
extensionPattern = re.compile(r'([.]png)$')

# Verifica ou cria a pasta
if not os.path.exists('pasta de png'):
    os.mkdir('pasta de pdf')

# Guarda o path absoludo da pasta
bag = os.path.abspath('pasta de pdf')

# Percorre toda árvore no diretório raiz
for folderName, subFolerNames, fileNames in os.walk('../..'):
    # Pega somente ficheiros
    for fileName in fileNames:
        # Analisa os arquivos correspondentes a png
        if extensionPattern.search(fileName):
            # Verifica a existencia do arquivo na pasta
            if not fileName in os.listdir(bag):
                # Copia os png para a pasta de png
                shutil.copy(os.path.join(folderName, fileName), bag)
