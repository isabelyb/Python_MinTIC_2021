import pandas as pd
df = pd.read_csv('/home/isa/Documents/MinTIC/Python_MinTIC/week_5/archivo.csv')
# print(df)
# print(df.columns)


diccionario = {'Nombres': ['Ana', 'Pedro', 'Juan'],
'Apellidos':['Cantillo', 'Charris', 'Juan'],
'edad':[20,50,18]}

df2 = pd.DataFrame(diccionario)
print(df2)

df2.to_csv('archivo_a_csv.csv')

df2.to_csv('archivo_a_csv.csv', sep='|')