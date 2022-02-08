import sys
import requests, bs4, webbrowser

print('Googling...') # exibe um texto enquanto faz dowload da pagina do Google
res = requests.get(f'http://google.com/search?q={"".join(sys.argv[1:])}')
res.raise_for_status()

# Obtém os links dos principais resultados da pesquisa
soup = bs4.BeautifulSoup(res.text, features='html.parser')


# Abre uma aba do navegador para cada resultado
linkElems = soup.select('a:has(h3)')
numOpen = 3
links = [a['href'] for a in linkElems]
for i in range(numOpen):
    webbrowser.open('http://google.com' + links[i])