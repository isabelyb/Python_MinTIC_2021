from functools import reduce


lista_0 = [(10,1,2),(10,3,4)]
lista_1 = [2,(10,1,2),(10,3,4)]
lista_2 = [
    [1,('a',1,2),('b',3,4)],
    [2,('c',5,6),('d',7,8)],
    [3,('e',9,10)]
    ]

def mult_1_2(lista):
    for i in lista:
        True
    return lista[1]*lista[2]

resultado_0 = [tuple(map(mult_1_2, lista_0))]
#print('lista_0:',resultado_0)
resultado_1 = [tuple(map(mult_1_2, lista_1[1:]))]


multiplicacion = [tuple(map(mult_1_2, (lista_2[i][1:]))) for i in range(len(lista_2))]

suma = [sum(multiplicacion[i]) for i in range(len(multiplicacion))]
print(suma)

numero = [lista_2[i][0] for i in range(len(lista_2))]
print(numero)

listado = list(zip(numero, suma))
print(listado)