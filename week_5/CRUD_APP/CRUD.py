#Librería con la lógica de las operaciones CRUD
###############################################


import json


'''ADICIONAR TAREA'''

#Adición de una tarea (Create)
def Create(tareas, identificador, tareaNueva):    
    tareas[identificador] = tareaNueva #Mutación del diccionario por referencia      


'''CONSULTAR TAREAS'''

#Consultar la información de todas las tareas (Read)
def Read(rutaArchivo='/home/isa/Documents/MinTIC/Python_MinTIC/week_5/CRUD_APP/listadoTareas.json'):

    #Cargar el listado de tareas a un diccionario desde la capa de datos (archivo JSON)    
    diccionarioTareas = {}#Contenedor del listado de tareas que gestiona la App
    try:    
        with open(rutaArchivo) as archivo:
            diccionarioTareas = json.load(archivo)  # json.load() carga el archivo
    except:
        print("No se pudo cargar la información de la capa de datos")
        return False #Reportar fallo en la carga

    #Retornar el contenedor o colección obtenido
    return diccionarioTareas


'''ACTUALIZAR TAREAS'''

#Actualizar una tarea específica (Update)
def Update(tareas, identificador, tareaActualizada): # tareaActualizada viene del formulario de la interfaz
    #Revisar los campos que llegan con información para actualizar
    for id_campo, campo in tareaActualizada.items():        
        if campo:
            tareas[identificador][id_campo] = campo #Actualizar el campo del diccionario (referencia)

'''ELIMINAR TAREAS'''            

#Eliminar una tarea específica (Delete)
def Delete(tareas, identificador):
    tareas.pop(identificador)
    print(f"\n>>> Tarea {identificador} eliminada <<<\n")


'''GRABAR LOS DATOS EN EL DICCIONARIO'''

#Operación de escritura en la capa de datos al cierre de la aplicación
def Write(tareas, rutaArchivo='/home/isa/Documents/MinTIC/Python_MinTIC/week_5/CRUD_APP/listadoTareas.json'):
    #Descargar contenedor de datos con las modificaciones realizadas por la App
    try:
        with open(rutaArchivo, 'w') as archivo_json:
            json.dump(tareas, archivo_json)
    except:
        print("Error: No se pudo guardar la información en la capa de datos.")
        return False
    
    #Si la escritura fue exitosa retorno correspondiente
    return True