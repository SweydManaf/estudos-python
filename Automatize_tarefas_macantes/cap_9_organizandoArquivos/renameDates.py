"""Renomeia os nomdes de arquivo com formato de data MM-DD-AAAA em estilo americano."""

import re
import os
import shutil

# Cria uma regex ue corresponda aos arquivos com formato de dta em estilo americano.
datePattern = re.compile(r"""
^(.*?) # todo o texto antes da data
((0|1)?\d)-     # um ou dois dígitos para o mês
((0|1|2|3)?\d)- # um ou dois dígitos para o dia
((19|20)\d\d)   # quatro dígitos para o ano
(.*?)$          # todo o texto após a data""", re.VERBOSE)


# Percorre os arquivos do diretório de trabalho com um loop
for amerFile in os.listdir('.'):
    mo = datePattern.search(amerFile)


    # Ignora os arquivos que não tenham uma data
    if mo == None:
        continue

    # Obtém os paths absolutos completos dos arquivos
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)


    # Compões o nome do arquivo em estilo europeu
    euroFileName = f'{beforePart}{dayPart}-{monthPart}-{yearPart}{afterPart}'
    absWorkingDir = os.path.abspath('.')
    amerFile = os.path.join(absWorkingDir, amerFile)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    # Renomeia os arquivos
    print(f'Renaming {amerFile} to {euroFileName}...')
    shutil.move(amerFile, euroFileName)