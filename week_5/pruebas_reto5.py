import pandas as pd


# Read as DataFrame. header=None para no usar la primera fila como nombre de columnas

datos = pd.read_csv('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv', header=None)
df = pd.DataFrame(datos)
df.columns = ['id_voluntario','nombre','codigo_playa','peso_recolectado']
#print(df)

df_voluntarios = df.groupby(df['codigo_playa']).count()
salida_1 = {df_voluntarios.index[i]:df_voluntarios['id_voluntario'][df_voluntarios.index[i]] for i in range(len(df_voluntarios))}
#print(salida_1)

df_peso = df.groupby(df['codigo_playa']).sum()
salida_2 = {df_peso.index[i]:df_peso['peso_recolectado'][df_peso.index[i]] for i in range(len(df_peso))}
#print(salida_2)

max_recolectado = max(df['peso_recolectado'])
salida_3 = {'Máximo recolectado en una playa': max_recolectado}
#print(salida_3)

total_recoleccion = sum(df['peso_recolectado'])
salida_4 = {'Total recolectado': total_recoleccion}
#print(salida_4)

total_voluntarios = df['id_voluntario'].count()
salida_5 = {'Total voluntarios': total_voluntarios}
#print(salida_5)