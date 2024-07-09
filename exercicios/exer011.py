class Funcionario:
    def __init__(self, nome, salario, percentual):
        self._nome = nome
        self._salario = salario
        self._percentual = percentual

    def _calcular_bonus(self):
        return self._salario * (self._percentual / 100)

    def exibir_detalhes(self):
        print('Nome: {}, Salário: R${:.2f}, Bônus: R${:.2f}'
              .format(self._nome, self._salario, self._calcular_bonus()))


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario, 15)


class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario, 10)


class Estagiario(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario, 7)
