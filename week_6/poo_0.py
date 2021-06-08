class persona:
    def __init__(self, nombre, edad):
        self.Nombre = nombre #atributos con init
        self.Edad = edad #atributos con init

    def imprimir(self): # método
        print('Hola, me llamo', self.Nombre)

objeto_1 = persona('Juan', 25)
objeto_2 = persona('Juana', 30)
objeto_3 = persona('Juanita', 5)

print(objeto_1.Nombre, objeto_1.Edad)
print(objeto_2.Nombre, objeto_2.Edad)
print(objeto_3.Nombre, objeto_3.Edad)

objeto_1.imprimir()
objeto_2.imprimir()
objeto_3.imprimir()


        