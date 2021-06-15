''' 
*archivo csv = 1234,Juan,921,5.4 -> id_voluntario, nombre, codigo_playa, peso_recolectado (por línea)
*url_archivo = https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv

**Requerimiento**. 

Se necesita leer el archivo csv, y obtener la siguiente información:
Opción 1: cuántos voluntarios se registraron en cada playa.
Opción 2: total de residuos recolectados en cada playa.
Opción 3: el máximo valor recolectado en una playa.
Opción 4: total recolectado en el evento.
Opción 5: total de voluntarios enlistados.

1. Función que reciba como parámetros la url del archivo y el código de la opción.
2. Construya un datframe
3. Obtenga la información descrita anteriormente según la opción escogida.
'''
import pandas as pd
import numpy as np

datos = pd.read_csv('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv')

def funcion1(ruta_archivo, opcion):
    salida = {}


    df = pd.DataFrame(datos)
    df.columns = ['id_voluntario','nombre','codigo_playa','peso_recolectado']

    salida = {}

    if opcion == 1:
        pass
#        salida = {codigo_playa: cantidad_voluntarios}
    elif opcion == 2:
         pass
#        salida = {codigo_playa: total_recolectado}
    elif opcion == 3:
        max_recolectado = max(df['peso_recolectado'])
        salida = {'Máximo recolectado en una playa': max_recolectado}
    elif opcion == 4:
        pass
#        salida = {'Total recolectado': xxxx}
    elif opcion == 5:
         pass
#        salida = {'Total voluntarios': xxxx}
    else:
        salida = {}


    


    return salida

#Salida: Dict Opción 1: {codigo_playa:cantidad_voluntarios, ...}  -> codigo_playa: int - cantidad_voluntarios: int



'''Casos Públicos'''
# print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',1))
# print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',2))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',3))
