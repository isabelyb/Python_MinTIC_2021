# elevar al cuadrado  los elementos de una  lista de tuplas

lista = [2,(10,1,2),(10,3,4)]
lista1 = [(2,2),(10,1,2),(10,3,4)]
# print(len(lista))
# print(len(lista[1]))
# print(range(len(lista[1])))
# print(range(1, (len(lista[1]))))

def cuad(numero):
    return numero**2

def mult(x,y):
    return x*y


lista_anidada1 = [ lista[i] for i in range(len(lista)) if i>0  ]
print('lista_anidada1',lista_anidada1)

lista_anidada2 = [ lista[i][1] for i in range(len(lista)) if i>0  ]
print('lista_anidada2', lista_anidada2)

lista_anidada3 = [ (lista[i][1])**2 for i in range(len(lista)) if i>0  ]
print('lista_anidada3',lista_anidada3)

print(lista[1][1],lista[2][1])
#map las pone al cuadrado a todas

lista_cuad = [tuple(map(cuad, (lista[i]))) for i in range(len(lista)) if i>0]
print('lista_cuad', lista_cuad)

lista_cuad = [tuple(map(cuad, (lista[1])))]
print('lista_cuad', lista_cuad)

lista_cuad = [tuple(map(cuad, (lista1[i]))) for i in range(len(lista1)) if i>0]
print('lista_cuad', lista_cuad)




# lista_anidada4 = [ lista[i][1]*lista[i][2] for i in range(len(lista)) if i>0  ]
# print('lista_anidada4',lista_anidada4)



# print(lista[1][1],lista[1][2])

# lista_mult = [tuple(map(mult,lista[i][1],lista[i][2])) for i in range(len(lista)) if i>0]
# print('lista_mult', lista_mult)














#imprimir lista[i][j]
# lista_anidada2 = [[(lista[i][j])**2 for j in range(1,len(lista[i])) if i>0]for i in range(1,len(lista))]
# print(lista_anidada2)

#multiplicar lista[i][1]*lista[i][2]
# lista_anidada3 = [[lista[i]*lista[j] for j in range(1,len(lista[i])) if i>0]for i in range(1,len(lista))]
# print(lista_anidada3)



# lista_cuad = [tuple(map(cuad, lista[i])) for i in range(len(lista)) if i>0]
# print(lista_cuad)

# lista_cuad = [[tuple(map(cuad, lista[i][j])) for j in range(1,len(lista[i])) if i>0] for i in range(1,len(lista))]
# print(lista_cuad)

#print(lista[1][1])
# elevar al cuadrado  los elementos [i] de una  lista de tuplas

# lista_cuad_i = [tuple(map(cuad, lista[i])) for i in range(len(lista)) if i>0]
# print(lista_cuad_i)


# multiplicar entre sí los elemendos de una lista de tuplas

# lista_mult_entresi = [tuple(map(mult, lista[i])) for i in range(len(lista))]
# print(lista_mult_entresi)