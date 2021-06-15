orden = [[1,("5464",4,30000),("8274",18,42000),("9744",9,150000)],
        [2,("5464",9,30000),("9744",9,150000)],
        [3,("5464",9,30000),("88112",11,45000)],
        [4,("8732",7,35000),("7733",11,80000),("88112",5,45000)]]


def mult_1_2(lista):
    for i in lista:
        True
    return lista[1]*lista[2]


cant_x_precio = [tuple(map(lambda x: x[1]*x[2], (orden[i][1:]))) for i in range(len(orden))]

suma_x_pedido = list(map(sum, cant_x_precio))

print(suma_x_pedido)

pedido = [orden[i][0] for i in range(len(orden))]

print(pedido)

listado = list(zip(pedido, suma_x_pedido))
print(listado)

respuesta = [list(listado[i]) if listado[i][1] > 1000000 else (listado[i][0], listado[i][1]+30000) for i in range(len(listado))]
print(respuesta)

print(type(respuesta[2]))