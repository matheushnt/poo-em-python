from datetime import datetime
import pytz
from random import randint

print('SISTEMA DE CONTA BANCÁRIA'.center(45, '-'))


class ContaBancaria:
    """
    Cria um objeto ContaBancaria para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do cliente.
        cpf (str): CPF do cliente.
        ag (int): Agência responsável pela conta do cliente.
        cc (int): Número da conta do cliente.
        saldo (int): Saldo disponível na conta do cliente.
        limite (int): Limite de Cheque Especial do cliente.
        transacoes (list): Histórico de Transações do cliente.
    """

    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, ag, cc):
        self.nome = nome
        self.cpf = cpf
        self.ag = ag
        self.cc = cc
        self._saldo = 0
        self._limite = None
        self._transacoes = []
        self.cartoes = []

    # Método Privado
    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def consultar_limite_cheque_especial(self):
        print(f'Seu limite de Cheque Especial: R${self._limite_conta():.2f}')

    def consultar_historico(self):
        print('Valor, Saldo, Data/Hora')
        for transacao in self._transacoes:
            print(transacao)

    def consultar_saldo(self):
        print(f'Seu saldo atual é de R${self._saldo:.2f}')

    def depositar(self, valor):
        self._saldo += valor
        print(f'Você depositou R${valor:.2f}')
        self._transacoes.append((
            valor,
            self._saldo,
            ContaBancaria.data_hora()
        ))

    def sacar(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você está com saldo insuficiente para sacar esse valor')
        else:
            self._saldo -= valor
            print(f'Você sacou R${valor:.2f}')
            self._transacoes.append((
                -valor,
                self._saldo,
                ContaBancaria.data_hora()
            ))

    def transferir(self, valor, conta_destino):
        # Conta remetente
        self._saldo -= valor
        self._transacoes.append((
            -valor,
            self._saldo,
            ContaBancaria.data_hora()
        ))
        # Conta Destinatária
        conta_destino._saldo += valor
        conta_destino.transacoes.append((
            valor,
            conta_destino._saldo,
            ContaBancaria.data_hora()
        ))


class CartaoCredito:
    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self._titular = titular
        self._numero = randint(
            1000000000000000,
            9999999999999999
        )
        self._validade = '{}/{}'.format(
            CartaoCredito.data_hora().month,
            CartaoCredito.data_hora().year + 4
        )
        self._cod_seguranca = '{}{}{}'.format(
            randint(0, 9),
            randint(0, 9),
            randint(0, 9)
        )
        self._limite = 1000
        self._senha = '1234'
        self._conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova Senha Inválida')


conta_matheus = ContaBancaria(
    nome='Matheus',
    cpf='111.222.333-45',
    ag=1234,
    cc=62087
)


conta_kayk = ContaBancaria(
    nome='Kayk',
    cpf='123.456.789-10',
    ag=1209,
    cc=32165
)


cartao_matheus = CartaoCredito(
    titular='Matheus',
    conta_corrente=conta_matheus
)
