import shutil
import os

# Copiando arquivos e pastas
shutil.copy()

shutil.copytree()

# Movendo e renomeando arquivos e pastas
shutil.move()

os.rename()

# Apagando arquivos e pastas permanentemente
os.unlink()

os.rmdir()
shutil.rmtree()

# Percorendo árvore de diretório
for folderName, subFolders, fileNames in os.walk('..'):
    print(f'Pasta atual: {folderName}')

    for subFolder in subFolders:
        print(f'Subpasta de {folderName}: {subFolder}')

    for fileName in fileNames:
        print(f'Dentro da pasta: {folderName}: {fileName}')

    print()