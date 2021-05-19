'''
Desarrollar un programa que permita cargar 5 nombres de personas y
sus edades respectivas.
Luego de realizar la carga por teclado de todos los datos imprimir los
nombres de las personas mayores de edad (mayores o iguales a 18
años)
'''
nombres = []
edades = []

i=0
while i<5:
    nom = input('Ingrese el nombre: ')
    nombres.append(nom)
    ed = int(input('Ingrese la edad: '))
    edades.append(ed)
    i +=1

print("Los mayores de edad son:")

for i in range(5):
    if edades[i]>=18:
        print(nombres[i],":",edades[i])


        