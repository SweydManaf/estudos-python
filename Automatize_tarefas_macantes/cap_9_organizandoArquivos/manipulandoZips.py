import os
import shutil
import zipfile


# Extraindo itens de arquivos ZIP

os.chdir('diretorio')
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()

# Criando arquivos ZIP e adicionando itens
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('arquivo', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

# Compactando uma pasta para ZIP
shutil.make_archive('pastaCompactada', 'zip', 'pasta')