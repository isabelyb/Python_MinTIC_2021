# Json : Javascript Object Notation

import json

datos = {}
datos['clientes'] = []
datos['clientes'].append({'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80'})
datos['clientes'].append({'codigo': '020008','nom': 'Carolina Charris','dir': 'cr 84 70 27 Bod 4'})
datos['clientes'].append({'codigo': '020114','nom': 'Omar Acosta','dir': 'cr 30 25 80'})

with open('datos.json','w') as file:
    json.dump(datos, file, indent=4)


# Para leerlo
with open('datos.json') as file:
    datos2 = json.load(file)

for i in datos2['clientes']:
    print(i['codigo'])
    print(i['nom'])
    print(i['dir'])

