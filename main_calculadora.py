
from Calculadora import Calculadora

# Solicitar dados do usuário
valorA = float(input("Digite o primeiro valor: "))
valorB = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação (+, -, *, /): ")

# Instância da classe Calculadora com valores fornecidos pelo usuário
calc = Calculadora(valorA, valorB, operacao)
calc.mostrarResultado()
