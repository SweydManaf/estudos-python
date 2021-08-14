import re

validateRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,25}$')
password = input("Insira sua senha: ")
verifyPassword = re.match(validateRegex, password)
if verifyPassword:
    print('\033[32mSua senha é valida!\033[m')
else:
    print('\033[31mSua senha é invalida!\033[m')