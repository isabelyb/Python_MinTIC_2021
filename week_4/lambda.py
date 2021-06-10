# lambda argumentos : cuerpo de la función




suma = lambda val1,val2: val1 + val2
operacion = lambda operacion, val1, val2: operacion(val1, val2)
resultado = operacion(suma, 10, 20)

z = lambda a,b,c: a + b + c
#print(z(1,2,3))
suma = lambda *args: sum(args)
#print(suma(3,4,5,6,7))
    
orden = [[1,("5464",4,30000),("8274",18,42000),("9744",9,150000)],
        [2,("5464",9,30000),("9744",9,150000)],
        [3,("5464",9,30000),("88112",11,45000)],
        [4,("8732",7,35000),("7733",11,80000),("88112",5,45000)]]
        
cant_x_precio = [tuple(map(lambda x: x[1]*x[2], (orden[i][1:]))) for i in range(len(orden))]
print(cant_x_precio)

 
