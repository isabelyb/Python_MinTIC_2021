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


def funcion1(ruta_archivo, opcion):

    datos = datos = pd.read_csv(ruta_archivo, header=None) 
    df = pd.DataFrame(datos)
    df.columns = ['id_voluntario','nombre','codigo_playa','peso_recolectado']

    if opcion == 1:
        df_voluntarios = df.groupby(df['codigo_playa']).count()
        salida = {df_voluntarios.index[i]:df_voluntarios['id_voluntario'][df_voluntarios.index[i]] for i in range(len(df_voluntarios))}
    elif opcion == 2:
        df_peso = df.groupby(df['codigo_playa']).sum()
        salida = {df_peso.index[i]:df_peso['peso_recolectado'][df_peso.index[i]] for i in range(len(df_peso))}
    elif opcion == 3:
        max_recolectado = max(df['peso_recolectado'])
        salida = {'Máximo recolectado en una playa': max_recolectado}
    elif opcion == 4:
        total_recoleccion = sum(df['peso_recolectado'])
        salida = {'Total recolectado': total_recoleccion}
    elif opcion == 5:
        total_voluntarios = df['id_voluntario'].count()
        salida = {'Total voluntarios': total_voluntarios}
    else:
        salida = {}


    return salida


'''Casos Públicos'''
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',1))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',2))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',3))


print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',4))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',5))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',6))