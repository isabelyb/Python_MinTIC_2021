import pandas as pd
import numpy as np


# Read as DataFrame. header=None para no usar la primera fila como nombre de columnas

datos = pd.read_csv('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv', header=None)
df = pd.DataFrame(datos)
df.columns = ['id_voluntario','nombre','codigo_playa','peso_recolectado']
#print(df)

max_recolectado = max(df['peso_recolectado'])
salida_3 = {'Máximo recolectado en una playa': max_recolectado}
#print(salida_3)

total_recoleccion = sum(df['peso_recolectado'])
salida_4 = {'Total recolectado': total_recoleccion}
print(salida_4)