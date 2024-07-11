import unittest
from exercicios.exer011 import (Funcionario,
                                Gerente, Desenvolvedor, Estagiario)


class TestFuncionario(unittest.TestCase):
    def setUp(self):
        self.funcionario = Funcionario('Bob', 30, 3000)

    def test_exibir_detalhes_funcionario(self):
        self.assertEqual(self.funcionario.exibir_detalhes(),
                         'Nome: Bob, Idade: 30 anos, Salário: R$3000.00')


class TestGerente(unittest.TestCase):
    def setUp(self):
        self.gerente = Gerente('Gil', 38, 8000, 'TI')

    def test_calcular_bonus_gerente(self):
        self.assertEqual(self.gerente.calcular_bonus(), 1600)

    def test_exibir_detalhes_gerente(self):
        self.assertEqual(self.gerente.exibir_detalhes(),
                         'Nome: Gil, Idade: 38 anos, Salário: R$8000.00')


class TestDesenvolvedor(unittest.TestCase):
    def setUp(self):
        self.desenvolvedor = Desenvolvedor('Ana', 25, 5000, 'Python')

    def test_calcular_bonus_desenvolvedor(self):
        self.assertEqual(self.desenvolvedor.calcular_bonus(), 600)

    def test_exibir_detalhes_desenvolvedor(self):
        self.assertEqual(self.desenvolvedor.exibir_detalhes(),
                         'Nome: Ana, Idade: 25 anos, Salário: R$5000.00')


class TestEstagiario(unittest.TestCase):
    def setUp(self):
        self.estagiario = Estagiario('Mat', 19, 1800, 'Estácio')

    def test_calcular_bonus_estagiario(self):
        self.assertEqual(self.estagiario.calcular_bonus(), 144)

    def test_exibir_detalhes_estagiario(self):
        self.assertEqual(self.estagiario.exibir_detalhes(),
                         'Nome: Mat, Idade: 19 anos, Salário: R$1800.00')


if __name__ == '__main__':
    unittest.main()
