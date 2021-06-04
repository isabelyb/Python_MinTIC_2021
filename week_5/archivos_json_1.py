import json

# Escribir archivos JSON con Python

data = {}
data['clients'] = []

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

with open('clientes.json', 'w') as file:
    json.dump(data, file, indent=4)


# Leer archivos JSON con Python

with open('clientes.json') as file:
    data = json.load(file)

    for client in data['clients']:
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('Amount:', client['amount'])
        print('')

# Codificación Unicode

data = {'first_name': 'Daniel', 'last_name': 'Rodríguez'}
json.dumps(data)

json.dumps(data, ensure_ascii=False)