# phoneAndEmail.py - Encontra os numeros de telefone e enderecos de email no clipboard

import re

phoneRegex = re.compile(r'''(
(\(\d{3}\)|\d{3})? # codigo de area
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
([a-zA-Z0-9._%+-]+) # nome do usuario
@           # simbolo @
([a-zA-Z0-9.-]+)   # nome do dominio
(\.com)   # ponto seguido de outros caracteres
)''', re.VERBOSE)

text = '''Para ver um exemplo, abra seu navegador web na página de contato da No
Starch Press em http://www.nostarch.com/contactus.htm, tecle CTRL-A para
selecionar todo o texto da página e CTRL-C para copiá-lo para o clipboard. Ao
executar esse programa, a saída será semelhante a:
Copied to clipboard:
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com'''

matches = []
for groups in phoneRegex.findall(text):
    print(groups)
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    print(phoneNum)
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    print(groups)
    print(groups[0])
    matches.append(groups[0])

for data in matches:
    print(data)


