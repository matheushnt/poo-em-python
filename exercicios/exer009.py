class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            print('Não foi possível alterar o nome do funcionário.')

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if isinstance(novo_salario, (int, float)) and novo_salario > 0:
            self.__salario = novo_salario
        else:
            print('Não foi possível alterar o salário do funcionário')


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, novo_bonus):
        if isinstance(novo_bonus, (int, float)) and novo_bonus > 0:
            self.__bonus = novo_bonus
        else:
            print('Não foi possível alterar o salário do gerente')
