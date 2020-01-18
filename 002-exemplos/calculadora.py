# Este código tem como objetivo construir uma calculadora em Python.

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Não é possível dividir {} / {} ".format(num1, num2))

# Validação das funções criadas
# Soma
assert soma(1, 1) == 2
assert soma(-1, -5) == -6
assert soma(0.5, 1) == 1.5

# Subtração
assert subtracao(1, 1) == 0
assert subtracao(-1, -5) == 4
assert subtracao(0.5, 1) == -0.5

# Multiplicação
assert multiplicacao(1, 1) == 1
assert multiplicacao(-1, -5) == 5
assert multiplicacao(0.5, 1) == 0.5

# Divisão
assert divisao(1, 1) == 1
assert divisao(-1, -5) == 0.2
assert divisao(0.5, 1) == 0.5