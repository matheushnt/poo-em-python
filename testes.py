import unittest
from exercicios.exer009 import Funcionario, Gerente


class TesteFuncionario(unittest.TestCase):
    def setUp(self):
        self.funcionario = Funcionario('Ana', 3000)

    def test_acessar_nome_funcionario(self):
        self.assertEqual(self.funcionario.nome, 'Ana')

    def test_acessar_salario_funcionario(self):
        self.assertEqual(self.funcionario.salario, 3000)

    def test_alterar_nome_funcionario(self):
        self.funcionario.nome = 'Beatriz'
        self.assertEqual(self.funcionario.nome, 'Beatriz')

    def test_alterar_salario_funcionario(self):
        self.funcionario.salario = 5000
        self.assertEqual(self.funcionario.salario, 5000)


class TesteGerente(unittest.TestCase):
    def setUp(self):
        self.gerente = Gerente('Eduardo', 5750, 1200)

    def test_acessar_nome_gerente(self):
        self.assertEqual(self.gerente.nome, 'Eduardo')

    def test_acessar_salario_gerente(self):
        self.assertEqual(self.gerente.salario, 5750)

    def test_acessar_bonus_gerente(self):
        self.assertEqual(self.gerente.bonus, 1200)

    def test_alterar_nome_gerente(self):
        self.gerente.nome = 'Thiago'
        self.assertEqual(self.gerente.nome, 'Thiago')

    def test_alterar_salario_gerente(self):
        self.gerente.salario = 6000
        self.assertEqual(self.gerente.salario, 6000)

    def test_alterar_bonus_gerente(self):
        self.gerente.bonus = 1350
        self.assertEqual(self.gerente.bonus, 1350)


if __name__ == '__main__':
    unittest.main()
