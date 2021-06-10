orden = [[1,("5464",4,30000),("8274",18,42000),("9744",9,150000)],
        [2,("5464",9,30000),("9744",9,150000)],
        [3,("5464",9,30000),("88112",11,45000)],
        [4,("8732",7,35000),("7733",11,80000),("88112",5,45000)]]

# print(orden[0][1][1]*orden[0][1][2] )
# print(orden[0][2][1]*orden[0][2][2] )
def multiplicar(orden):
    for i in range(len(orden)):
        for j in range(1,(len(orden[i]))):
            print(orden[i][j][1]*orden[i][j][2])
    return 

#multiplicar(orden)

lista = [(1,2),(3,2)]

def mult(numero):
    return numero * numero

lista_multiplicada = [tuple(map(mult, lista[i])) for i in range(len(lista))]
print(lista_multiplicada)

#orden_multiplicada = list(map(multiplicar, orden))

# print(len(orden))
# print(range(len(orden)))

# print(len(orden[0]))
# print(range(len(orden[0])))
# print(range(1,(len(orden[0]))))

# print(len(orden[1]))
# print(range(len(orden[1])))
# print(range(1,(len(orden[1]))))

#orden = [1,("5464",4,30000),("8274",18,42000),("9744",9,150000)]

#  Multiplicar cantidad de item x precio en cada pedido

# lista = [1,('a',2, 50),('b',4,100)]

# # orden = [[1,("5464",2,100),("8274",2,50),("9744",3,200)],
# #         [2,("5464",1,20),("9744",4,500)]]

# #print(range(1,len(lista)))
