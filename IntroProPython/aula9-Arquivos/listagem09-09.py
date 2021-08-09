pagina = open('pagina.html', 'w', encoding='utf-8')
pagina.write('''
<!DOCTYPE html>
<html lan="br">
<head>
<meta charset="utf-8">
<title>Titulo da Pagina</title>
</head>
<body>
Ola!
''')
for l in range(10):
    pagina.write(f'<p>{l}</p>')
pagina.write('''
</body>
</html>
''')
pagina.close()