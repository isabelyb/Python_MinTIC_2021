# status_sensores = (1,0,0,1,0)

# cant_sensores = len(status_sensores)


# activos = sum(status_sensores)


# salida = []
datos = [
    {'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1, 'sensores': 7},
    {'codigo1': '020008','nom': 'Carolina Charris','dir': 'cr 84 70 27 Bod 4','zona': 2,'sensores': 5},
    {'codigo2': '030011','nom': 'Juan Pérez','dir': 'cr 30 10 80','zona': 3,'sensores': 5},
    {'codigo': '020114','nom': 'Omar Acosta','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
    {'codigo': '020115','nom': 'Camilo Fernández','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
    {'codigo': '010020','nom': 'Juan Díaz','dir': 'cr 30 15 80','zona': 1,'sensores': 8}]

# for i in range(len(datos)):
#     if datos[i]['codigo'] == '010020':
#         salida.append({'zona': datos[i]['zona'], 'nombre': datos[i]['nom']})



lista = []
dic_unido = {}
for clientes in datos:
    dic_unido.update(clientes)

lista.append(dic_unido.copy())

print(dic_unido)
print(lista)
print(datos)

# copia = datos.copy()
# print(copia)