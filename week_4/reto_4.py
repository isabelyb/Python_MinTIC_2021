# orden = [número de pedido,(código del artículo, cantidad, precio por unidad), ... (código del artículo, cantidad, precio por unidad)],

# Requerimiento. Se necesita conocer el número de pedido y la cantidad total del mismo.

orden = [[1,("5464",4,30000),("8274",18,42000),("9744",9,150000)],
        [2,("5464",9,30000),("9744",9,150000)],
        [3,("5464",9,30000),("88112",11,45000)],
        [4,("8732",7,35000),("7733",11,80000),("88112",5,45000)]]

orden_1 = [[1,("5464",1,30000),("8274",2,42000),("9744",3,150000)],
        [2,("7733",3,80000),("88112",10,45000),("5464",2,30000),("9744",9,150000)],
        [3,("88112",25,45000)],
        [4,("5464",9,30000),("9744",20,150000)],
        [5,("8732",7,35000),("7733",11,80000),("88112",5,45000)]]


# ------------------ VERSIÓN 1 --------------------- #

def facturarTotal(orden):
 
    cant_x_precio = [tuple(map(lambda x: x[1]*x[2], (orden[i][1:]))) for i in range(len(orden))]

    suma_x_pedido = list(map(sum, cant_x_precio))

    pedido = [orden[i][0] for i in range(len(orden))]

    listado = list(zip(pedido, suma_x_pedido))

    respuesta = [list(listado[i]) if listado[i][1] > 1000000 else (listado[i][0], listado[i][1]+30000) for i in range(len(listado))]

    return respuesta


print(facturarTotal(orden))
print(facturarTotal(orden_1))

# ------------------ VERSIÓN 2 --------------------- #

def facturarTotal(orden):

    cant_x_precio = [tuple(map(lambda x: x[1]*x[2], (orden[i][1:]))) for i in range(len(orden))]

    suma_x_pedido = list(map(sum, cant_x_precio))

    fletes = [suma_x_pedido[i]+30000 if suma_x_pedido[i] < 1000000 else suma_x_pedido[i] for i in range(len(suma_x_pedido))]

    pedido = [orden[i][0] for i in range(len(orden))]

    listado = list(zip(pedido, fletes))

    respuesta = [list(listado[i]) if listado[i][1] > 1000000 else listado[i] for i in range(len(listado))]
    
    return respuesta

print(facturarTotal(orden))
print(facturarTotal(orden_1))