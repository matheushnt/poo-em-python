import unittest
from exercicios.exer010 import Empresa, Funcionario


class TestEmpresa(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa('Math Motors')
        self.func1 = Funcionario('Ana')
        self.func2 = Funcionario('Bob')

    def test_adicionar_funcionario(self):
        self.empresa.adicionar_funcionario(self.func1)
        self.assertIn('Ana', self.empresa.listar_funcionarios())

    def test_nao_adicionar_funcionario_nao_instanciado(self):
        self.empresa.adicionar_funcionario('Carlos')
        self.assertNotIn('Carlos', self.empresa.listar_funcionarios())

    def test_remover_funcionario(self):
        self.empresa.adicionar_funcionario(self.func1)
        self.empresa.adicionar_funcionario(self.func2)
        self.empresa.remover_funcionario('Bob')
        self.assertIn('Ana', self.empresa.listar_funcionarios())
        self.assertNotIn('Bob', self.empresa.listar_funcionarios())

    def test_listar_funcionarios(self):
        self.empresa.adicionar_funcionario(self.func1)
        self.empresa.adicionar_funcionario(self.func2)
        self.assertEqual(['Ana', 'Bob'], self.empresa.listar_funcionarios())


if __name__ == '__main__':
    unittest.main()
