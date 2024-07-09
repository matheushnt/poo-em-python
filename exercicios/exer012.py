class Biblioteca:
    def __init__(self):
        self._livros = []

    def _verificar_senha(f):
        def wrapper(self, *args, **kwargs):
            senha = kwargs.get('senha', '')
            if senha == 'lib333':
                return f(self, *args, **kwargs)
            else:
                print('Acesso negado. Insira a senha correta.')
        return wrapper

    @_verificar_senha
    def adicionar_livro(self, titulo, autor, senha=''):
        self._livros.append({'titulo': titulo, 'autor': autor})

    @_verificar_senha
    def remover_livro(self, titulo, senha=''):
        self._livros = [
            livro for livro in self._livros if livro['titulo'] != titulo
        ]

    def listar_livros(self):
        return self._livros
