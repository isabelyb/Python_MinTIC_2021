def estado_nivel(datos_tanque: dict) -> dict:
    dicSalida = {'codigoTanque': datos_tanque['codigo'], 'nivel': ' '}
    if(datos_tanque['sensor1'] == False and datos_tanque['sensor2'] == False and datos_tanque['sensor3'] == False):
        dicSalida['nivel'] = 'vacío'
    elif(datos_tanque['sensor1'] == True and datos_tanque['sensor2'] == False and datos_tanque['sensor3'] == False):
        dicSalida['nivel'] = 'nivel bajo'
    elif(datos_tanque['sensor1'] == True and datos_tanque['sensor2'] == True and datos_tanque['sensor3'] == False):
        dicSalida['nivel'] = 'nivel medio'
    elif(datos_tanque['sensor1'] == True and datos_tanque['sensor2'] == True and datos_tanque['sensor3'] == True):
        dicSalida['nivel'] = 'nivel alto'
    else:
        dicSalida['nivel'] = 'revisar sensores'
    return f"Estado del nivel del líquido del tanque {dicSalida['codigoTanque']}: {dicSalida['nivel']}"
