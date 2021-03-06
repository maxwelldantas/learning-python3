"""
Uma classe é uma estrutura que abstrai um conjunto de objetos com características similares.
"""


class Livro:

    # Construção da classe Livro com seus respectivos atributos, self faz referência à própria classe Livro
    def __init__(self, titulo, autor, editora, isbn, ano):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.isbn = isbn
        self.ano = ano

    # Para retornar o objeto Livro em formato de String
    def __str__(self):
        return 'Titulo: %s, Autor: %s, Editora: %s, ISBN: %s, Ano: %s' % \
               (self.titulo, self.autor, self.editora, self.isbn, self.ano)


Livro1 = Livro('Curso de Python em 6h', 'Alcimar Costa', 'Udemy', '878-98-9988-988-9', 2018)

print(Livro1)
print(Livro1.titulo)
print(Livro1.autor)
print(Livro1.editora)
print(Livro1.isbn)
print(Livro1.ano)
