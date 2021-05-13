"""Crear un diccionario que contenga los precios por kilo de 4 frutas. 
El programa debe preguntar al usuario que fruta desea y 
cuántos kilos necesita Cree una función que devuelva 
el precio que debe pagar el usuario. 
Si la fruta no está en el diccionario debe mostrar el mensaje
que no hay existencias de la fruta 
Utilice input para capturar los datos
"""

def calcular_precio(precio_fruta, cantidad):
    precio_pagar = precio_fruta * cantidad
    return precio_pagar
    
fruta = input("buenos días qué fruta quiere comprar hoy?: ")
cantidad = int(input("cuantos kilos desea comprar?:"))
precios_frutas = {
    "Banano": 1200,
    "Papaya": 900,
    "Naranja": 2000,
    "Manzana": 5500
}

if fruta in precios_frutas:
    pagar = calcular_precio(precios_frutas[fruta], cantidad)
    print(f"El precio a pagar es {pagar}")
else:    
    print("No hay existencias de esta fruta") 


# frutas = {
#      'chirimoya': 5000, 'mangostino': 2000, 'banano': 200, 'piña': 1500 
#      } 
     
# def fruteria(fruta: str, cantidad: int): 
#     if fruta in frutas: 
#         precio = int(cantidad) * frutas[fruta] 
#         return f"Son {precio}" 
#     else: 
#         return f"No hay existencia de esa fruta" 
        
# print(fruteria(input('Que fruta desea? '), input('cuantas quiere? ')))         


