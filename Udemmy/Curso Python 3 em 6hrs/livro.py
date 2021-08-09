class Livro():
   def __init__(self, titulo, autor, editora, isbn, ano):
      self.titulo = titulo
      self.autor = autor
      self.editora = editora
      self.isbn = isbn
      self.ano = ano

   def __str__(self):
      return f'Titulo: {self.titulo}, Editora: {self.editora} ' \
             f'ISBN: {self.isbn}, Ano: {self.ano}'


