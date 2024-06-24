class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descrever(self):
        print(f'{self.marca} {self.modelo}')


class Carro(Veiculo):
    def __init__(self, nome, modelo, portas):
        super().__init__(nome, modelo)
        self.portas = portas

    def descrever(self):
        super().descrever()
        print(f'Carro com {self.portas} portas')


class Moto(Veiculo):
    def __init__(self, nome, modelo, cilindradas):
        super().__init__(nome, modelo)
        self.cilindradas = cilindradas

    def descrever(self):
        super().descrever()
        print(f'Moto com {self.cilindradas} cilindradas')


carro1 = Carro('Toyota', 'Corolla', 4)
carro1.descrever()

moto1 = Moto('Kawasaki', 'Ninja', 400)
moto1.descrever()
