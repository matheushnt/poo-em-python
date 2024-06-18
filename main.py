from exercicios.exer002 import Livro

# Arquivo criado para testar a funcionalidade das classes

livro1 = Livro(titulo='Duna', autor='Frank Herbert', paginas=544)
livro2 = Livro(titulo='Sun Tzu ', autor='A Arte da Guerra', paginas=160)
livro3 = Livro(titulo='Guerra do Velho', autor='John Scalzi', paginas=368)

livro1.exibir_detalhes()
livro2.exibir_detalhes()
livro3.exibir_detalhes()
print(f'Quantidade de Livros: {Livro.total_livros()}')
