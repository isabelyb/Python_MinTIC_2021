
print("Hello, world!")


# Elevar a potencia en Python

x = 5**8
print(x)


# Máximo y Mínimo
maximum = max(1,2,3,4)
print(maximum)

minimum = min(1,2,3,4)
print(minimum)

#Función Help

    # help(print)

number_range = range(20)

for number in number_range:
    print(number)

print("La cantidad de valores es: ", len(number_range))


# FUNCIONES


def percentage():
    """Función que saca el porcentaje de un valor"""
    result = int((10*730000)/100)
    print("El 10% de $ 730000 es:", result, "pesos")


def greetings():
    print("Buenas!")

def greetings_and_percentage():
    print("Buenas!")
    result = int((10*730000)/100)
    print("El 10% de $ 730000 es:", result, "pesos")


if __name__ == '__main__':
    percentage()
    greetings()
    greetings_and_percentage()


# Asignar varios valores a varias variables

var1, var2, var3 = 10, 20 , 30
print(var1, var3)


# Ejercicios rápidos

    #Variables
x = 43
x = x + 1 
print(x) # 44


    #Promedios
var1, var2, var3, var4 = 10, 4, 5.5, 67

result1 = (var1 + var2 + var3 + var4)/4
print("Resultado 1: El promedio de estos números es: ", result1)

list = 10, 4, 5.5, 67
result2 = (10 + 4 + 5.5 + 67)/(len(list))
print("Resultado 2: El promedio de estos números es: ", result2)

list = [10, 4, 5.5, 67]
result3 = sum(list)/len(list)
print("Resultado 3: El promedio de estos números es: ", result3)

import statistics

list1 = [10, 4, 5.5, 67]
result4 = statistics.mean(list1)
print("Resultado 4: El promedio de estos números es: ", result4)

    # área y perímetro de un cuadrado :  L = 38 m

        # A = L * L
        # P = L + L + L + L

side = 38
area = 38**2
perimeter = 38*4

print("El área del cuadrado es", area, " metros cuadrados \nEl perímetro del cuadrado es", perimeter, "metros")

