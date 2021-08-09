from VideoAulas.Udemmy.livro import Livro

livro1 = Livro('Curso de Python em 6h', 'Alcimar Costa', 'Udemy',
               '878-98-9988-988-9', 2018)

livro2 = Livro('Python web', 'Alcimas Costa', 'Udemy',
               '878-98-9988-988-9', 2018)

livro3 = Livro('Inteligencia Artificial', 'Alcimas Costa', 'Udemy',
               '878-98-9988-988-9', 2018)

livros = [livro1, livro2, livro3]

for l in livros:
    print(l)