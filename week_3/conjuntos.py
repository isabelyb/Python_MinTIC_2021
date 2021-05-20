# from typing import Type

# # Los conjuntos no son indexados
# Tupla1 = 4, 5, 6, 3

# # Set es la orden para convertir en conjunto
# conjunto = set([4,5,8,9])
# conjunto4 = set('Hola mundo, Hola mundo')
# print(conjunto4)

# conjunto2 = {7, 8, 9, 6, 7, True, (4,5,6)}

# print(type(Tupla1), type(conjunto2), type(conjunto))

# #Unifica datos repetidos
# conjunto3 = set([4,5,8,9, 1, 4, 4, 4, 1, 1])
# print(conjunto3)

# #Se recorre con for
# for i in conjunto:
#     print(i)

# for i in conjunto4:
#     print(i)

# #Adicionar items
# conjunto.add('Hola')
# print(conjunto)


a = {2, 3, 5, 6, 7, 0}
b = {2, 5, 12, 34, 56}

#Unión de conjuntos
c = a|b
print(c)

d = a&b
print(d)