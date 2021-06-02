"""Realizar una aplicación que dada una lista con diccionarios de datos y una tupla con identificaciones, cree una nueva lista en donde solo esten los datos de las identificaciones de la tupla.
"""

datos = [
    {"id":32569874, "nombre": "Juan Castro", "celular": 3012354690},
    {"id":45687975, "nombre": "Rosalinda García", "celular": 3028564690},
    {"id":45897625, "nombre": "pepito Perez", "celular": 3032346558},
    {"id":45896741, "nombre": "Samuel Ochoa", "celular": 3082355698}]

identificacion = (32569874, 45896741)

# for i in range(4):
#     print(datos[i]["id"])

# for i in range(0,2):
#     print(identificacion[i])



nueva_lista = []
for i in range(4):
    if datos[i]["id"] in identificacion:
        nueva_lista.append(datos[i])
print(nueva_lista)


nueva_lista1 = []
for i in range(4):
    if datos[i]["id"] in identificacion:
        nueva_lista1.append(datos[i])
print(nueva_lista1)