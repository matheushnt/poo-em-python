class Empresa:
    def __init__(self, nome):
        self._nome = nome
        self.__funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.__funcionarios.append(funcionario)
        else:
            print(
                'Apenas instâncias da classe Funcionario podem ser adicionadas'
            )

    def remover_funcionario(self, nome):
        self.__funcionarios = [
            f for f in self.__funcionarios if f._nome != nome
        ]

    def listar_funcionarios(self):
        return [f._nome for f in self.__funcionarios]


class Funcionario:
    def __init__(self, nome):
        self._nome = nome
