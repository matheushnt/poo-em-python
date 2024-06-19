class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print('O novo salário deve ser maior que zero.')
