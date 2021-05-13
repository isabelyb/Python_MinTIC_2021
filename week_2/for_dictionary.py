datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}

clave = datos_basicos.keys()            # llaves
valor = datos_basicos.values()          # valores              
cantidad_datos = datos_basicos.items()  # agrupa todo en una lista
cantidad = len(datos_basicos)

for clave, valor in cantidad_datos:
    print(f"{clave}: {valor}")

print(cantidad)

# cantidad = sum(map(len, numeros.values()))
# print(cantidad)

for clave in cantidad_datos:
    print(f"{clave}: {datos_basicos} ")   # error para corregir