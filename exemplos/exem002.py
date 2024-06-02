print('CRIANDO CLASSES'.center(30, '-'))
# O método __init__() é o método construtor da classe, sendo essencial para
# inicializar o objeto criado com valores definidos


class Pessoa:
    # Método construtor
    def __init__(self):
        self.nome = 'Caio'
        self.idade = 25
        self.sexo = 'M'


pessoa1 = Pessoa()
print(pessoa1.nome)
pessoa2 = Pessoa()
pessoa2.nome = 'Ana'
pessoa2.idade = 10
pessoa2.sexo = 'M'
print(f'{pessoa2.nome} tem {pessoa2.idade} anos de idade')


print('=-' * 20)


class Veiculo:
    # Método construtor
    def __init__(self, marca, nome, cor, ano, dimensao, kilometragem, motor):
        self.marca = marca
        self.nome = nome
        self.cor = cor
        self.ano = ano
        self.dimensao = dimensao
        self.kilometragem = kilometragem
        self.motor = motor


carro = Veiculo('Toyota', 'Corolla', 'Preto', 2024, 'Sedan', 20000, 2.0)
print(carro.marca, carro.nome)
