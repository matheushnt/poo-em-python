from exercicios.exer004 import Produto

# Arquivo criado para testar a funcionalidade das classes

prod1 = Produto(nome='PlayStation 5', preco=3699)
prod2 = Produto(nome='Cadeira Gamer', preco=1199)

prod1.preco = '3200'
prod2.nome = ''

print(prod1.preco)
print(prod2.nome)

prod1.preco = 3270
prod2.nome = 'Nintendo Switch'

print(prod1.preco)
print(prod2.nome)
