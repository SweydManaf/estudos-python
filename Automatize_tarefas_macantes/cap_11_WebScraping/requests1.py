# Fazendo download de uma pagina web com a função requests.get()

import requests

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

# Verficando se houve erros
try:
    res.raise_for_status()
except Exception as exc:
    print(f'There was a problem: {exc}')
    exit(1)

# url work: https://automatetheboringstuff.com/files/rj.txt
print(f'Workig: {res.status_code == requests.codes.ok}')
print(f'Length: {len(res.text)}')
print(f'First 250 lines: \n\t{res.text[:250]}')

