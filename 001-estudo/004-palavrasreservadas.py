# Aprendendo sobre as palavras reservadas em Python
# https://howtodoinjava.com/python/python-keywords/

# and
x = ( 0 > 5 and 5 < 10 )
print("Intervalo de 0 a 10 - and")

# or
x = ( 0 > 5 or 5 < 10 )
print("Intervalo de 0 a 10 - or")

# as - é usado para criar um alias.
import calendar as cal
print(cal.month_name[1])

# assert - é usado para debuggar um código
x = "Passou"
# assert x == "Passou o Avião"

# async

# await

# class - é usado para criar uma classe
 
# def - é usado para criar ou declarar uma função
def soma(a, b):
    return a + b

print(soma(1, 1))

# del
x = "Nota 10"
print(x)
del x 
# print(x) NameError: name 'x' is not defined

# if - é usado como o comando condicional Se

# elif - é usado como o comando condicional Senão Se

# else - Senão

# try

# except


# finally

# raise

# False - é usado para definir o valor booleano False 

# True - é usado para definir o valor booleano True

# for - é usado para criar um for loop

# while - é usado para criar um while loop

# break - é usado para parar o while

# continue - é usado para continuar um fluxo

# import - é usado para importar módulos

# from - é usado para importar um especifico módulo.

# global - é usado para definir uma variavel global

# in - são utilizadas com dois propositos
# 1. é usado para checar se o valor está presente uma lista
# 2. é usado para iterar sobre uma lista com for loop

frutas = [ "banana", "maça", "pera", "uva" ]
if "banana" in frutas:
    print("sim tem banana na lista")
 
for x in frutas:
    print(x)

# is - é usado para testar se dois objetos referenciam o mesmo objeto
print("is\n")
a = ["apple", "banana", "cherry"]
b = ["apple", "banana", "cherry"]
c = a
 
print(a is b)   # False
print(a is c)   # True

# lambda

# None - é usado para definir a variável como null
x = None
 
if x:
  print("Do you think None is True")
else:
  print("None is not True...")      # Prints this statement

# nonlocal

# not - é usado como um operador lógico que reverte o valor booleano

# pass

# return - é usado para retornar um valor em uma função

# with

# yield