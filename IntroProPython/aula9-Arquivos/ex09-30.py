filmes = {
    'drama': ['Cidadao Kane', 'O Poderoso Chefao'],
    'comedia': ['Tempos Modernos', 'American Pie', 'Dr. Dolittle'],
    'policial': ['Chuva negra', 'Desejo de Matar', 'Dificil de Matar'],
    'guerra': ['Rambo', 'Platoon', 'Tora!Tora!Tora!']
}

pagina = open('pagina.html', 'w', encoding='utf-8')
pagina.write('''
<!DOCTYPE html>
<html lan="br">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
Ola!
''')
for c, v in filmes.items():
    pagina.write(f'<h1>{c}</h1>')
    pagina.write('<ul>')
    for e in v:
        pagina.write(f'<li>{e}</li>')
    pagina.write('</ul>')
pagina.write('''
</body>
</html>
''')
pagina.close()