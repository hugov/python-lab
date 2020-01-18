# Aprendendo sobre a manipulação de string em Python
# https://howtodoinjava.com/python/python-strings/

# Declaração de variável string
str = 'Teste de string'
print(str)
print(type(str)) # <class 'str'>

str = "Teste de string"
print(str)
print(type(str)) # <class 'str'>

# Função (Método) substring
str = 'Olá mundo'
print(str[2:5])

# Função para tratamento de array
print(str[0])   # O

# Função para tratamento de tamanho da string
print(len(str))   # 9

# Função para formatar a string
nome = "Vitor Hugo"
idade = 36

msg = "Olá {} você tem {} anos."
print(msg.format(nome, idade))

msg = "Eu tenho {1} anos e meu nome é {0} ."
print(msg.format(nome, idade))