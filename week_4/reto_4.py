# orden = [número de pedido,(código del artículo, cantidad, precio por unidad), ... (código del artículo, cantidad, precio por unidad)],

# Requerimiento. Se necesita conocer el número de pedido y la cantidad total del mismo.

orden = [[1,("5464",4,30000),("8274",18,42000),("9744",9,150000)],
        [2,("5464",9,30000),("9744",9,150000)],
        [3,("5464",9,30000),("88112",11,45000)],
        [4,("8732",7,35000),("7733",11,80000),("88112",5,45000)]]


def facturarTotal(orden):
    pass

def mult_1_2(lista):
    for i in lista:
        True
    return lista[1]*lista[2]

multiplicacion = [tuple(map(mult_1_2, (orden[i][1:]))) for i in range(len(orden))]

suma = [sum(multiplicacion[i]) for i in range(len(multiplicacion))]
print(suma)

numero = [orden[i][0] for i in range(len(orden))]
print(numero)

listado = list(zip(numero, suma))
print(listado)



