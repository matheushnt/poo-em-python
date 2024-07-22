class Pagamento:
    def __init__(self, destino, valor):
        self.destino = destino
        self.valor = valor


class PagamentoBoleto(Pagamento):
    def __init__(self, destino, valor, codigo_barras):
        super().__init__(destino, valor)
        self.codigo_barras = codigo_barras

    def processar_pagamento(self):
        return 'Processando pagamento de R${:.2f} com boleto {}.'.format(
            self.valor,
            self.codigo_barras
        )


class PagamentoCartao(Pagamento):
    def __init__(self, destino, valor, num):
        super().__init__(destino, valor)
        self.num = num

    def processar_pagamento(self):
        return 'Processando pagamento de R${:.2f} com cartão {}.'.format(
            self.valor,
            self.num[-4:]
        )


class PagamentoPix(Pagamento):
    def __init__(self, destino, valor, chave_pix):
        super().__init__(destino, valor)
        self.chave_pix = chave_pix

    def processar_pagamento(self):
        return 'Processando pagamento de R${:.2f} com chave {}.'.format(
            self.valor,
            self.chave_pix,
        )
