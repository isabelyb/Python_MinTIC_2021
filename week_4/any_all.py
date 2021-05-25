# print(all([True, True, True])) # True si todos los elementos son True
# print(all([True, False, True]))
# print(any([True, False, True])) # True si algún elemento es True
# print(any([False, False, False]))

# print(all([])) # True
# print(any([])) # False

'''Se recibe una lista de números enteros separados por espacios: Si todos los enteros
son positivos, se debe revisar si algún entero es un número palíndromo
 Se imprime ‘True’ si se cumplen las condiciones o 
 ‘False’ de lo contrario
'''

# No entendí esto  - buscar .split()

info = [int(input())].split(' ')

print('True' if all(list(map(lambda x:x>0, list(map(int, info[1])))))  and  any(list(map(lambda x: x[0]==x[1]  or  x[0] == '5', list(zip(info[1], list(map(lambda x:x[-1:(len(x)+1)*-1:-1], info[1]))))))) else 'False')

# No entendí esto


