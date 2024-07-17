import unittest
from exercicios.exer013 import Veiculo, Carro, Moto, Caminhao


class TestVeiculo(unittest.TestCase):
    def setUp(self):
        self.veiculo = Veiculo('Toyota', 'SW4', 2020)

    def test_exibir_detalhes(self):
        self.assertEqual(self.veiculo.calcular_consumo(350, 20), 17.5)


class TestCarro(unittest.TestCase):
    def setUp(self):
        self.carro = Carro('Chevrolet', 'Trailblazer', 2025, 'SUV')

    def test_exibir_detalhes(self):
        self.assertEqual(self.carro.detalhes(), 'Marca: Chevrolet, Modelo: Trailblazer, Ano: 2025, Carroceria: SUV')

    def test_calcular_consumo(self):
        self.assertEqual(self.carro.calcular_consumo(420), 35)


class TestMoto(unittest.TestCase):
    def setUp(self):
        self.moto = Moto('Kawasaki', 'Ninja', 2023, 300)

    def test_exibir_detalhes(self):
        self.assertEqual(self.moto.detalhes(), 'Marca: Kawasaki, Modelo: Ninja, Ano: 2023, Cilindradas: 300')

    def test_calcular_consumo(self):
        self.assertEqual(self.moto.calcular_consumo(290), 14.5)


class TestCaminhao(unittest.TestCase):
    def setUp(self):
        self.caminhao = Caminhao('Scania', 'Linha S', 2023, 'Truck')

    def test_exibir_detalhes(self):
        self.assertEqual(self.caminhao.detalhes(), 'Marca: Scania, Modelo: Linha S, Ano: 2023, Classificação: Truck')

    def test_calcular_consumo(self):
        self.assertEqual(self.caminhao.calcular_consumo(782), 97.75)


if __name__ == '__main__':
    unittest.main()
