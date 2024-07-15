import unittest
from exercicios.exer012 import Biblioteca


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.lib = Biblioteca()
        self.livro1 = {'titulo': 'Livro A', 'autor': 'Math'}
        self.livro2 = {'titulo': 'Livro B', 'autor': 'Bob'}

    def test_adicionar_livro_com_senha_correta(self):
        self.lib.adicionar_livro(self.livro1['titulo'], self.livro1['autor'], senha='lib333')
        self.lib.adicionar_livro(self.livro2['titulo'], self.livro2['autor'], senha='lib333')
        self.assertIn(self.livro1, self.lib._livros)
        self.assertIn(self.livro2, self.lib._livros)

    def test_adicionar_livro_com_senha_incorreta(self):
        self.lib.adicionar_livro(self.livro1['titulo'], self.livro1['autor'], senha='errada')
        self.lib.adicionar_livro(self.livro2['titulo'], self.livro2['autor'], senha='errada')
        self.assertNotIn(self.livro1, self.lib._livros)
        self.assertNotIn(self.livro2, self.lib._livros)

    def test_remover_livro_com_senha_correta(self):
        self.lib.adicionar_livro(self.livro1['titulo'], self.livro1['autor'], senha='lib333')
        self.lib.remover_livro('Livro A', senha='lib333')
        self.assertNotIn(self.livro1, self.lib._livros)

    def test_remover_livro_com_senha_incorreta(self):
        self.lib.adicionar_livro(self.livro2['titulo'], self.livro2['autor'], senha='lib333')
        self.lib.remover_livro('Livro B', senha='errada')
        self.assertIn(self.livro2, self.lib._livros)

    def test_listar_livros(self):
        self.lib.adicionar_livro(self.livro1['titulo'], self.livro1['autor'], senha='lib333')
        self.lib.adicionar_livro(self.livro2['titulo'], self.livro2['autor'], senha='lib333')
        lista_livros = self.lib.listar_livros()
        self.assertIn(self.livro1, lista_livros)
        self.assertIn(self.livro2, lista_livros)


if __name__ == '__main__':
    unittest.main()
