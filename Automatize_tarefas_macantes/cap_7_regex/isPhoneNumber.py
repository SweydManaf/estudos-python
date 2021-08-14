import re

message = 'My number is 415-555-4242'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)

print(f'Phone number found: {mo.group()}')
print('-='*30)

# --------- Agrupando com parenteses ----------------
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My computer is 415-555-4242.')

print(f'Grupo 1: {mo.group(1)}')
print(f'Grupo 2: {mo.group(2)}')
print(f'Grupo 0: : {mo.group(0)}')
print(f'Grupo: {mo.group()}')
print(f'Todos grupo: {mo.groups()}')
