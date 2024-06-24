from random import randint


class Agencia:
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self._caixa = 0
        self._emprestimos = []

    def verificar_caixa(self):
        if self._caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual: R${:.2f}'
                  .format(self._caixa))
        else:
            print(f'Caixa atual: R${self._caixa:.2f}')

    def emprestar(self, cpf, valor, juros):
        if self._caixa > valor:
            self._caixa -= valor
            self._emprestimos.append((cpf, valor, juros))
        else:
            print('Empréstimo negativado. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        super().__init__(telefone, cnpj, 1000)
        self.site = site
        self._caixa = 1000000
        self._caixa_paypal = 0

    def depositar_paypal(self, valor):
        self._caixa -= valor
        self._caixa_paypal += valor
        print(f'Você depositou R${valor:.2f}')

    def sacar_paypal(self, valor):
        self._caixa += valor
        self._caixa_paypal -= valor
        print(f'Você sacou R${valor:.2f}')


class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self._caixa = 1000000


class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self._caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio >= 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Cliente não tem o patrimônio mínimo para entrar na Agência')


if __name__ == '__main__':
    ag1 = Agencia(
        telefone=40028922,
        cnpj=34785771000153,
        numero=245
    )

    ag_virtual = AgenciaVirtual(
        site='www.agenciavirtual.com.br',
        telefone='08004500',
        cnpj=71912966000143
    )

    ag_comum = AgenciaComum(
        telefone='08006500',
        cnpj=94717265000159
    )

    ag_premium = AgenciaPremium(
        telefone='08005500',
        cnpj=89738163000180
    )
