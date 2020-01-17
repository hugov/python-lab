# Aprendendo sobre os tipos de dados em Python
# https://howtodoinjava.com/python/python-data-types/

x = 'A'
y = "B"
z = """
    C
    """

print(x)
print(y)
print(z)

print(x + y)

print(x*3) #Imprime AAA - repetição de operadores

name = str('john')  # Construtor
print(name)
 
somaItens = str(100)   # Conversão de int para string
print(somaItens)

x = 100+3j # Tipo definido como complexo
print(x)

# list, tuple, range

itens = [ "Melão" , "Ovo", "Coca Cola" ]
print(itens) # Imprime ['Melão', 'Ovo', 'Coca Cola']

alfabeto = [ "a", "b", "c", "d", "e", "f", "g" ]
print(alfabeto[:3]) # Imprime o range ['a', 'b', 'c']
print(alfabeto[2:5]) # Imprime o range ['c', 'd', 'e']

# Tuple - é uma lista que somente permite leitura
itensTuple = ( 1, "um", 2, "três" )
print(itensTuple[0:2])

# dict
carrosMap = { 1 : "Audi - A3", 2 : "BMW - X6", 3 : "Ford - Mustang" }
print(carrosMap[1]) # Imprime Audi - A3
print(carrosMap.keys()) # Imprime dict_keys([1, 2, 3])
print(carrosMap.values()) # Imprime dict_values(['Audi - A3', 'BMW - X6', 'Ford - Mustang'])

# set, frozenset
digitos = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(digitos) # Imprime o resultado: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(type(digitos)) # Imprime o resultado: <class 'set'>

digitos.remove(0)    # Remove o primeiro elemento
print(digitos) # Imprime o resultado: {1, 2, 3, 4, 5, 6, 7, 8, 9}

digitosImutaveis = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
# digitosImutaveis.remove(0) # AttributeError: 'frozenset' object has no attribute 'remove'

# Nota:
# frozenset - Este atributo torna o set imutavel, ou seja, não permite a remoção de nenhum dos seus elementos

# bool
verdadeiro = True
falso = False

print(verdadeiro)
print(falso)

# bytes, bytearray, memoryview
x = b'char_data'
x = b"char_data"
 
y = bytearray(5)
 
z = memoryview(bytes(5))
 
print(x)    # b'char_data'
print(y)    # bytearray(b'\x00\x00\x00\x00\x00')
print(z)    # <memory at 0x014CE328>

print(type(x))
print(type(y))
print(type(z))

# type
x = 5
print(type(x))          # <class 'int'>
 
y = 'howtodoinjava.com'
print(type(y))          # <class 'str'>