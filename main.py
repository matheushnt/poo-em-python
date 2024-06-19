from exercicios.exer003 import Funcionario

# Arquivo criado para testar a funcionalidade das classes

func_matheus = Funcionario(nome='Matheus', salario=1000)

print(func_matheus.salario)
func_matheus.salario = -1000

print(func_matheus.salario)

func_matheus.salario = 2500
print(func_matheus.salario)    # Novo salário
