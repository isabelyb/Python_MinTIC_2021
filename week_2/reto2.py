datos_tanque = {
    'codigo': 'TA001',
    'sensor1':True,
    'sensor2':True,
    'sensor3':False
    }

def estado_nivel(datos_tanque):
    dicSalida={
        'codigoTanque':"",
        'nivel':""
    }

    if datos_tanque['sensor1'] == False and datos_tanque['sensor2'] == False and datos_tanque['sensor3'] == False:
        dicSalida['codigoTanque'] = datos_tanque['codigo']
        dicSalida['nivel'] = "vacío"

    elif datos_tanque['sensor1'] == True and datos_tanque['sensor2'] == False and datos_tanque['sensor3'] == False:
        dicSalida['codigoTanque'] = datos_tanque['codigo']
        dicSalida['nivel'] = "nivel bajo"        

    elif datos_tanque['sensor1'] == True and datos_tanque['sensor2'] == True and datos_tanque['sensor3'] == False:
        dicSalida['codigoTanque'] = datos_tanque['codigo']
        dicSalida['nivel'] = "nivel medio"

    elif datos_tanque['sensor1'] == True and datos_tanque['sensor2'] == True and datos_tanque['sensor3'] == True:
        dicSalida['codigoTanque'] = datos_tanque['codigo']
        dicSalida['nivel'] = "nivel alto"

    else:
        dicSalida['codigoTanque'] = datos_tanque['codigo']
        dicSalida['nivel'] = "revisar sensores"      

    return f"Estado del nivel del líquido del tanque {dicSalida['codigoTanque']}: {dicSalida['nivel']}"



print(estado_nivel(datos_tanque))