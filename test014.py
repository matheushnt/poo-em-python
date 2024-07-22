import unittest
from exercicios.exer014 import Pagamento, PagamentoBoleto, PagamentoCartao, PagamentoPix


class TestPagamento(unittest.TestCase):
    def setUp(self):
        self.pgmt = Pagamento('Mat', 250)

    def test_verificar_comporvante(self):
        self.assertEqual(self.pgmt.verificar_comprovante(), 'Destino: Mat, Valor: 250.00')


class TestPagamentoBoleto(unittest.TestCase):
    def setUp(self):
        self.boleto = PagamentoBoleto('Mat', 250, '00190500954014481606906809350314337370000000100')

    def test_verificar_comprovante(self):
        self.assertEqual(self.boleto.verificar_comprovante(), 'Destino: Mat, Valor: 250.00')

    def test_processar_pagamento(self):
        self.assertEqual(self.boleto.processar_pagamento(),
                         'Processando pagamento de R$250.00 com boleto 00190500954014481606906809350314337370000000100.'
                         )


class TestPagamentoCartao(unittest.TestCase):
    def setUp(self):
        self.cartao = PagamentoCartao('Mat', 250, '5571225791834501')

    def test_verificar_comprovante(self):
        self.assertEqual(self.cartao.verificar_comprovante(), 'Destino: Mat, Valor: 250.00')

    def test_processar_pagamento(self):
        self.assertEqual(self.cartao.processar_pagamento(),
                         'Processando pagamento de R$250.00 com cartão 4501.'
                         )


class TestPagamentoPix(unittest.TestCase):
    def setUp(self):
        self.pix = PagamentoPix('Mat', 250, 'hob2357@gmail.com')

    def test_verificar_comprovante(self):
        self.assertEqual(self.pix.verificar_comprovante(), 'Destino: Mat, Valor: 250.00')

    def test_processar_pagamento(self):
        self.assertEqual(self.pix.processar_pagamento(),
                         'Processando pagamento de R$250.00 com chave hob2357@gmail.com.'
                         )


if __name__ == '__main__':
    unittest.main()
