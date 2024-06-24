class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def fazer_som(self):
        print(f'{self.nome} faz {self.som}')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome, 'miau miau')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, 'au au')


gatinho = Gato('Bixano')
cachorrinho = Cachorro('Xodó')

gatinho.fazer_som()
cachorrinho.fazer_som()
