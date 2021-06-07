'''
Cómo podríamos acceder directamente a la llave de un diccionario que hace parte de una lista compuesta por muchos diccionarios, sin necesidad de recorrer toda la lista..?

¿ Con una llave que recibo como parámetro al invocar una función, podría "ubicar" esa llave directamente en el archivo json sin necesidad de leerlo todo ?
'''

dictionary = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4',
}

search = 'key2'

if search in dictionary:
    print(f'Value for "{search}" is {dictionary[search]}')
else:
    print(f'Your search "{search}" did not match any values')
