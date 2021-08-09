import re

nakamotoregex = re.compile(r'(([A-Z])\w* Nakamoto)')

nakamotofamily = nakamotoregex.findall('''Satoshi Nakamoto Alice Nakamoto 
RoboCop Nakamoto 
mas não a 
satoshi Nakamoto em que o primeiro nome não começa com letra
maiúscula 
Mr. Nakamoto em que a palavra anterior tem um caractere que não é 
uma letra Nakamoto que não tem primeiro nome Satoshi nakamoto em que 
Nakamoto não começa com letra maiúscula''')


for groups in nakamotofamily:
    print(groups[0])