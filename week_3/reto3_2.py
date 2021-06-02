datos = [
    {'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1, 'sensores': 7},
    {'codigo': '020008','nom': 'Carolina Charris','dir': 'cr 84 70 27 Bod 4','zona': 2,'sensores': 5},
    {'codigo': '030011','nom': 'Juan Pérez','dir': 'cr 30 10 80','zona': 3,'sensores': 5},
    {'codigo': '020114','nom': 'Omar Acosta','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
    {'codigo': '020115','nom': 'Camilo Fernández','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
    {'codigo': '010020','nom': 'Juan Díaz','dir': 'cr 30 15 80','zona': 1,'sensores': 8}]


codigo = '020008'
sensores = (0,0,0,1,0)

def monitoreo(codigo,sensores):
    activos = sum(sensores)
    salida = []
    lista = []

    for i in range(len(datos)):
        if datos[i]['codigo'] == codigo:
            if activos == 0:
                lista.append({})
            else:
                salida.append({'codigo_cliente': codigo, 'direccion': datos[i]['dir']})

                if datos[i]['zona'] == 1:
                    salida.append({'cantidad_guardias':'3 guardias'})
                else:
                    salida.append({'cantidad_guardias':'2 guardias'})

                
                salida.append({'sensores_activos': activos})


                if datos[i]['sensores'] == len(sensores):
                    salida.append({'estado_sensores':'correcto'})
                else:
                    salida.append({'estado_sensores':'revisar'})

                unir_diccionarios = {}
                for diccionario in salida:
                    unir_diccionarios.update(diccionario)

                lista.append(unir_diccionarios.copy())

                print(unir_diccionarios)
                print(salida)

    return lista
        
print(monitoreo(codigo,sensores))
    
