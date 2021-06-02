import pandas as pd

diccionario = {'Nombres': ['Ana', 'Pedro', 'Juan'],
'Apellidos':['Cantillo', 'Charris', 'Juan'],
'edad':[20,50,18]}

df = pd.DataFrame(diccionario, index=['Cliente1', 'Client2','Client3'])

df.to_excel('archivo_a_excel.xlsx', sheet_name='Clientes' )