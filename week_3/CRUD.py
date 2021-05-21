'''Un CRUD son acciones aplicables a una base de datos, en este caso temporal
C  Create
R  Read
U  Update
D  Delete
'''

'''CRUD para tareas, manejando un diccionario:
'''

tareas = {
    1: { 
            'descripcion':'Ir a mercar',
            'estado' : 'pendiente',
            'tiempo' : 60            
           },
    2: { 
            'descripcion':'Estudiar',
            'estado' : 'pendiente',
            'tiempo' : 180            
           }, 
    3: { 
            'descripcion':'Hacer ejercicio',
            'estado' : 'pendiente',
            'tiempo' : 50            
           } 
}

# Funciones
def crear(tareas, identificador, tarea_nueva):
    tareas[identificador] = tarea_nueva
    return tareas

def leer(tareas):
    for i in tareas:  # i toma los valores de las tareas
        print(i,"-\t",end="")
        for j in tareas[i]: # toma los valores de los valores
            print(tareas[i][j], "| ", end="")
        print()

def buscar(identificador, tareas):
    con_identificadores = set(tareas.keys())
    if identificador in con_identificadores:
        return True
    else:
        return False

def actualizar(tareas, identificador, nuevo_estado, nueva_descripción, nuevo_tiempo):
    tareas[identificador]["descripcion"] = nueva_descripción
    tareas[identificador]["estado"] = nuevo_estado
    tareas[identificador]["tiempo"] = nuevo_tiempo
    return print("\n<<<<TAREA ACTUALIZADA>>>>\n")  

def eliminar_tarea(identificador):
    for i in tareas:
        if identificador == tareas[i]:
            del tareas[identificador]
    print(tareas[i])
    print (f"\nLa tarea {tareas[identificador]} ha sido satisfactoriamente eliminada\n")
    
# Interfaz - Menú
estado = True
while estado:
    print("\n<<<<APLICACIÓN CRUD - MANEJO DE TAREAS>>>>\n")
    print("1. Adicionar tarea")
    print("2. Consultar tarea")
    print("3. Actualizar tarea")
    print("4. Eliminar tarea")
    print("5. Salir\n")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 5:
        estado = False
        
    elif opcion == 1:
        identificador = int(input("Ingrese el identificador de la tarea: "))
        descripción = input("Ingrese la descripción de la tarea: ")
        estado = input("Ingrese el estado inicial de la tarea: ")
        tiempo = int(input("Ingrese el tiempo de ejecución: "))
        tarea_nueva = {
            "descripcion": descripción,
            "estado": estado,
            "tiempo": tiempo
        }

        tareas = crear(tareas, identificador, tarea_nueva)
        print("\n<<<<TAREA ADICIONADA>>>>\n")

    elif opcion == 2:        
        print("\n<<<<LISTADO DE TAREAS>>>>\n")
        leer(tareas) 

    elif opcion == 3:
        print("\n<<<<ACTUALIZAR TAREA>>>>\n")
        identificador = int(input("Ingrese el Identificador de la tarea a modificar: "))
        if buscar(identificador, tareas):
            nueva_descripción = input("Ingrese la nueva descripción de la tarea: ")
            nuevo_estado = input("Ingrese el nuevo estado inicial de la tarea: ")
            nuevo_tiempo = int(input("Ingrese el nuevo tiempo de ejecución: "))
            actualizar(tareas, identificador, nuevo_estado, nueva_descripción, nuevo_tiempo)
        else:
            print("\nLa tarea no existe\n")
            

    elif opcion == 4:
        print("\n<<<<ELIMINAR TAREA>>>>\n")
        identificador = int(input("Ingrese el Identificador de la tarea a eliminar: "))
        eliminar_tarea(identificador)


    else:
        print("Digite una opción válida\n")


print(tareas)