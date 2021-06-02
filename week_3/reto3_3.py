datos = [
    {'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1, 'sensores': 7},
    {'codigo': '020008','nom': 'Carolina Charris','dir': 'cr 84 70 27 Bod 4','zona': 2,'sensores': 5},
    {'codigo': '030011','nom': 'Juan Pérez','dir': 'cr 30 10 80','zona': 3,'sensores': 5},
    {'codigo': '020114','nom': 'Omar Acosta','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
    {'codigo': '020115','nom': 'Camilo Fernández','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
    {'codigo': '010020','nom': 'Juan Díaz','dir': 'cr 30 15 80','zona': 1,'sensores': 8}]


codigo = '020008'
sensores = (0,0,1,0,0)

def monitoreo(codigo,sensores):
    activos = sum(sensores)
    diccionario = {}
    lista = []
    lista.append(diccionario)

    for i in range(len(datos)):
        if datos[i]['codigo'] == codigo:
            if activos == 0:
                diccionario.update({})
            else:
                diccionario.update({'codigo_cliente':codigo, 'direccion':datos[i]['dir']})
                if datos[i]['zona'] == 1:
                    diccionario.update({'cantidad_guardias':'3 guardias'})
                else:
                    diccionario.update({'cantidad_guardias':'2 guardias'})

                diccionario.update({'sensores_activos':activos})

                if datos[i]['sensores'] == len(sensores):
                    diccionario.update({'estado_sensores':'correcto'})
                else:
                    diccionario.update({'estado_sensores':'revisar'})
                    
    return lista


print(monitoreo('020008',(1,0,1,0,0,0,0)))        
print(monitoreo('020115',(0,0,0,0,0)))
    
