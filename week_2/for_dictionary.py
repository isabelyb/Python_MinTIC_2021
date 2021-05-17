datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}

# clave = datos_basicos.keys()            # llaves
# print(clave)
# valor = datos_basicos.values()          # valores
# print(valor)           
# cantidad_datos = datos_basicos.items()  # agrupa todo en una lista
# print(cantidad_datos)
# cantidad = len(datos_basicos)
# print(cantidad)

# for clave, valor in cantidad_datos:
#     print(f"{clave}: {valor}")


#acceder a la clave mediante el valor:

def print_llaves(val):
    for clave, valor in datos_basicos.items():
        if val == valor:
            return clave
            
    return "La clave no existe"        
                  
print(print_llaves("Leonardo Jose"))
 