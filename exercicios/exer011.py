class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def exibir_detalhes(self):
        return f'Nome: {self.nome}, Idade: {self.idade} anos, Salário: R${self.salario:.2f}'


class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, departamento):
        super().__init__(nome, idade, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return self.salario * 0.20


class Desenvolvedor(Funcionario):
    def __init__(self, nome, idade, salario, linguagem):
        super().__init__(nome, idade, salario)
        self.linguagem = linguagem

    def calcular_bonus(self):
        return self.salario * 0.12

class Estagiario(Funcionario):
    def __init__(self, nome, idade, salario, universidade):
        super().__init__(nome, idade, salario)
        self.universidade = universidade

    def calcular_bonus(self):
        return self.salario * 0.08
