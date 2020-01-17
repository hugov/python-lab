# Declaração e associação de variáveis

nome = "Vitor Hugo Oliveira"
idade = 36
sexo = 'M'
salario = 36800.00 # Sonho meu :)

print(nome)
print(idade)
print(sexo)
print(salario)

# Cadeia de associações de variáveis

x = y = z = 10
print(x)
print(y)
print(z)

# Multiplas associações de variáveis

nome, idade = "Sirley", 20
print(nome)
print(idade)

# Variável Global

i = 10

def soma():
    global j
    j = 15
    print(j)

soma()

print("Soma i + j = " + str(i + j))