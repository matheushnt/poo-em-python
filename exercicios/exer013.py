class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def calcular_consumo(self, km, km_litro):
        return km / km_litro


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, carroceria):
        super().__init__(marca, modelo, ano)
        self.carroceria = carroceria

    def detalhes(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Carroceria: {self.carroceria}'

    def calcular_consumo(self, km):
        if self.carroceria == 'SUV' or self.carroceria == 'Picape':
            return super().calcular_consumo(km, 12)
        elif self.carroceria == 'Hatch' or self.carroceria == 'Crossover':
            return super().calcular_consumo(km, 15)
        elif self.carroceria == 'Sedan':
            return super().calcular_consumo(km, 17)


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def detalhes(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cilindradas: {self.cilindradas}'

    def calcular_consumo(self, km):
        return super().calcular_consumo(km, 20)


class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, classificacao):
        super().__init__(marca, modelo, ano)
        self.classificacao = classificacao

    def detalhes(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Classificação: {self.classificacao}'

    def calcular_consumo(self, km):
        return super().calcular_consumo(km, 8)
