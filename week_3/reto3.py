datos = [
    {'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1, 'sensores': 7},
    {'codigo': '020008','nom': 'Carolina Charris','dir': 'cr 84 70 27 Bod 4','zona': 2,'sensores': 5},
    {'codigo': '030011','nom': 'Juan Pérez','dir': 'cr 30 10 80','zona': 3,'sensores': 5},
    {'codigo': '020114','nom': 'Omar Acosta','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
    {'codigo': '020115','nom': 'Camilo Fernández','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
    {'codigo': '010020','nom': 'Juan Díaz','dir': 'cr 30 15 80','zona': 1,'sensores': 8}]


codigo = '020008'
sensores = (1,0,0,1,1,0)

def monitoreo(codigo,sensores):
    salida = []
    lista = []

    for i in range(len(datos)):
        if datos[i]['codigo'] == codigo:
            salida.append({'codigo_cliente': codigo, 'direccion': datos[i]['dir']})

            if datos[i]['zona'] == 1:
                salida.append({'cantidad_guardias':'3 guardias'})
            else:
                salida.append({'cantidad_guardias':'2 guardias'})

            
            salida.append({'sensores_activos': sum(sensores)})


            if datos[i]['sensores'] == len(sensores):
                salida.append({'estado_sensores':'correcto'})
            else:
                salida.append({'estado_sensores':'revisar'})

            unir_diccionarios = {}
            for diccionario in salida:
                unir_diccionarios.update(diccionario)

            lista.append(unir_diccionarios.copy())

    return lista
        
print(monitoreo(codigo,sensores))
    

# [{'codigo_cliente': '020008', 'direccion': 'cr 84 70 27 Bod 4', 'cantidad_guardias': '2 guardias', 'sensores_activos': 2, 'estado_sensores': 'revisar'}]
    
    
    
    
    # if activos == 0:
    #     salida = [{}]
        




    # else:    
    #     if datos['zona'] == 1:
    #         cantidad_guardias = '3 guardias'
    #     else:
    #         cantidad_guardias = '2 guardias'

    #     if sensores == len(activos):
    #         estado_sensores = 'correcto'
    #     else:
    #         estado_sensores = 'revisar'
    
    



# [{'codigo_cliente': '020008', 'direccion': 'cr 84 70 27 Bod 4', 'cantidad_guardias': '2 guardias', 'sensores_activos': 2, 'estado_sensores': 'revisar'}]