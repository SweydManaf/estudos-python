"""Copia uma pasta toda e seu conteudo para um arquivo ZIP cujo nome seja incrementado"""

import os
import zipfile

def backupToZip(folder):
    # Faz backup de todo conteúdo de 'folder' em um arquivo ZIP.

    # Determina o nome do arquivo que esse codigo deverá usar
    # de acordo com os arquivos já existentes
    number = 1
    while True:
        zipFileName = folder + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1

    # Cria o arquivo ZIP
    print(f'Creating {zipFileName}...')
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Percorre toda a árvore de diretório e compacta os arquivos de cada pasta
    for folderName, subFolders, fileNames in os.walk(folder):
        print(f'Adding files in {folderName}')

        # Acrescenta a pasta atual ao arquivo ZIP
        backupZip.write(folderName)

        # Acrescenta todos os arquivos dessa pasta ao arquivo ZIP
        for fileName in fileNames:
            newBase = folder + '_'
            if fileName.startswith(newBase) and fileName.endswith('.zip'):
                continue
            backupZip.write(os.path.join(folderName, fileName))
    backupZip.close()
    print('Done')

if __name__ == '__main__':
    backupToZip('pasta')