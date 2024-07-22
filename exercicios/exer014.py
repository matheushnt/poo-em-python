class Pagamento:
    def __init__(self, destino, valor):
        self.destino = destino
        self.valor = valor

    def verificar_comprovante(self):
        return f"Destino: {self.destino}, Valor: {self.valor:.2f}"


class PagamentoBoleto(Pagamento):
    def __init__(self, destino, valor, codigo_barras):
        super().__init__(destino, valor)
        self.codigo_barras = codigo_barras

    def processar_pagamento(self):
        return f'Processando pagamento de R${self.valor:.2f} com boleto {self.codigo_barras}.'


class PagamentoCartao(Pagamento):
    def __init__(self, destino, valor, num):
        super().__init__(destino, valor)
        self.num = num

    def processar_pagamento(self):
        return f'Processando pagamento de R${self.valor:.2f} com cartão {self.num[-4:]}.'


class PagamentoPix(Pagamento):
    def __init__(self, destino, valor, chave_pix):
        super().__init__(destino, valor)
        self.chave_pix = chave_pix

    def processar_pagamento(self):
        return f'Processando pagamento de R${self.valor:.2f} com chave {self.chave_pix}.'
