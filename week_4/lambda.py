# lambda argumentos : cuerpo de la función

suma = lambda val1=0, val2=0 : val1 + val2

operacion = lambda operacion, val1=0, val2=0  : operacion(val1, val2)

resultado = operacion(suma, 10, 20)

print(resultado)


z = lambda a,b,c: a + b + c
print(z(1,2,3))


suma = lambda *args: sum(args)
print(suma(3,4,5,6,7))