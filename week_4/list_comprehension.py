'''Cree una lista con cuadrados de los números, de dos en dos, del 4 al 30, que son divisibles entre 3
'''

mi_lista = []
for x in range(4, 31, 2):
    if x%3 == 0:
        mi_lista.append(x**2)

print(mi_lista)

'''Cree un diccionario en el que las llaves sean una tupla entre los números del 3 al 10 y su respectivo cubo. Y dónde los valores sean las listas con los cuadrados de los números de dos en dos, entre el 4 y el 30, que son divisibles enteros con el primer elemento de su llave correspondiente.
'''

mi_diccionario = dict()
for y in range(3, 11):
    mi_diccionario[(y, y**3)] = []
    for x in range(4, 31, 2):
        if x%y == 0:
            mi_diccionario[(y, y**3)].append(x**2)

print(mi_diccionario)


# En una sola línea:

mi_lista = [x**2 for x in range(4, 31, 2) if x%3 == 0]
print(mi_lista)

mi_diccionario = { (y, y**3) : [x**2 for x in range(4, 31, 2) if x%y == 0] for y in range(3, 11) }
print(mi_diccionario)
