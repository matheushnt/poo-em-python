from datetime import date, timedelta
from random import randint


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.chave = None

    def pagar(self, destino, valor, modalidade):
        if modalidade.upper() == 'BOLETO':
            boleto = PagamentoBoleto(destino, valor)
            return f'Destino: {destino}, Valor: R${valor:.2f}, Vencimento: {boleto.vencimento()}, Numero: {
                boleto.numero}'


class Pagamento:
    def __init__(self, destino, valor):
        self.destino = destino
        self.valor = valor

    @staticmethod
    def data_atual():
        return date.today()


class PagamentoBoleto(Pagamento):
    def __init__(self, destino, valor):
        super().__init__(destino, valor)
        self.numero = randint(1000000000000000000000000000000000000000000000000,
                              9999999999999999999999999999999999999999999999999)

    def vencimento(self):
        dias = timedelta(days=3)
        return (PagamentoBoleto.data_atual() + dias).strftime('%d/%m/%Y')


class PagamentoCartao(Pagamento):
    pass


class PagamentoPix(Pagamento):
    def __init__(self, origem, destino, valor):
        super().__init__(origem, destino, valor)

    def pagar(self, valor, chave_pix):
        ...


if __name__ == '__main__':
    matheus = Usuario('Matheus')

    print(matheus.pagar('Kayk', 100, 'Boleto'))
