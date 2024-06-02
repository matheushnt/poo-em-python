print('CRIANDO MÉTODOS'.center(30, '='))
"""Self em Classes
Quando você cria uma classe em Python e cria um método dentro
dessa classe, self é uma maneira de sereferir ao objeto atual da classe.
Pense nele como "eu mesmo"."""


class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def cumprimentar(self):
        print('Olá, meu nome é {}, tenho {} anos e trabalho como {}'.format(
            self.nome, self.idade, self.profissao
        ))

    def agradecer(self):
        print('Muito obrigado(a)')


pessoa1 = Pessoa(nome='Joaquim', idade=45, profissao='Engenheiro Civil')
pessoa2 = Pessoa(nome='Isadora', idade=39, profissao='Pesquisadora')
pessoa1.cumprimentar()
pessoa1.agradecer()
pessoa2.cumprimentar()
pessoa2.agradecer()

print(pessoa1.idade)
print(pessoa2.profissao)

# OBS: para acessar um atributo de uma instância, não utiliza-se parênteses.
# Diferente de acessar um método, neste caso, precisa-se utilizar parênteses.
