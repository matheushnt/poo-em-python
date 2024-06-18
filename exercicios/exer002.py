class Livro:
    qtde_livros = 0

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Livro.qtde_livros += 1

    def exibir_detalhes(self):
        print('Título: {}, Autor: {}, Páginas: {}'
              .format(self.titulo, self.autor, self.paginas))

    @classmethod
    def total_livros(cls):
        return cls.qtde_livros
