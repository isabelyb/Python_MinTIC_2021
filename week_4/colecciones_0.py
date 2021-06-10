from math import pow

'''map: transforma el valor de cada elemento en otro
    map(función a aplicar, objeto iterable)
'''
# Obtener el cuadrado de todos los elementos de la lista

def cuadrado(elemento):
    return elemento * elemento

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = list(map(cuadrado, lista))
print(resultado)

# map y lambda:

resultado = list(map(lambda elemento: elemento * elemento, lista))
print(resultado)

# map con mas de un argumento y una lista:


numeros = [2,3,4]
potencias = [3,2,4]

pot = pow(2, 3)
print(pot)

potenciados = map(pow, numeros, potencias)
print(list(potenciados))

'''filter: realizar un filtro sobre los elementos, retornando booleano.
    filter(función a aplicar, objeto iterable)
'''

# Obtener la cantidad de elementos mayores a 5

def mayor_a_cinco(elemento):
    return elemento > 5

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado = tuple(filter(mayor_a_cinco, tupla))
print(len(resultado))
print('filter', resultado)

# filter y lambda:

resultado = tuple(filter(lambda elemento: elemento > 5, tupla))
print(resultado)

items = [1,2,3,4,5,6]
pares = tuple(filter(lambda x: x%2 == 0, items))
print(pares)

'''reduce: reducir elementos de una colección (acumulador). En una colección de elementos se requiere un único resultado
    reduce(función a aplicar(acumulador), objeto iterable)
'''

# Obtener la suma de todos los elementos de la lista
lista = [1,2,3,4]
acumulador = 0

for elemento in lista:
    acumulador += elemento

print(acumulador)

#

from functools import reduce

def f_acumulador(acumulador, elemento):
    return acumulador + elemento

resultado = reduce(f_acumulador, lista)
print(resultado)

# reduce y lambda:
resultado = reduce(lambda acumulador, elemento: acumulador + elemento, lista)
print(resultado)

lista = ['Python ', 'Java ', 'Ruby ', 'Elixir']
resultado1 = reduce(lambda acumulador, elemento: acumulador + elemento, lista)
print(resultado1)

'''zip: reorganizar listas, en tuplas
    zip(lista1, lista2, ..., lista_n)
'''
# Unir listas: nombre + apellido

nombres = ['Jose', 'Pepe', 'Juan']
apellidos = ['Perez', 'Sanchez Caro', 'Gonzalez']

nombre_apellido = list(zip(nombres, apellidos))
print(nombre_apellido)

a = [2,4,6]
b = [1,3,5]

c = list(zip(a,b))
print(c)

d = list(c[1])
print(d)