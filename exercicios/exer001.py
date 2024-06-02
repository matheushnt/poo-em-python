class ContaBancaria:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print(f'Seu saldo atual é de R${self.saldo:.2f}')

    def depositar(self, valor):
        self.saldo += valor
        print(f'Você depositou R${valor:.2f}')

    def sacar(self, valor):
        self.saldo -= valor
        print(f'Você sacou R${valor:.2f}')


conta_matheus = ContaBancaria(nome='Matheus', cpf='111.222.333-45')
conta_matheus.depositar(100)
conta_matheus.consultar_saldo()
conta_matheus.depositar(50)
conta_matheus.consultar_saldo()
conta_matheus.sacar(40)
conta_matheus.consultar_saldo()
