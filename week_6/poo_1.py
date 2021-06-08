#Implementar una clase que represente un empleado
class Empleado:

    # Definir como atributos su nombre y su sueldo
    # En el método __init__ (constructor) cargar los atributos por teclado
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ") #Atributo
        self.sueldo = float(input("Ingrese el valor del sueldo: ")) #Atributo

    # En otro método, imprimir sus datos
    def imprimir_datos(self):
        print("Nombre: ", self.nombre)
        print("Sueldo: ", self.sueldo)

    # Implementar un tercer método que imprima un mensaje si debe pagar 
    # impuestos (si el sueldo supera a 3000) 
    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")

    #Adicional: Saludar si no paga impuestos
    def saludar(self):
        print("Hola!")

            

#Bloque principal

pepe = Empleado()
pepe.imprimir_datos()
pepe.paga_impuestos()

maria = Empleado()
maria.imprimir_datos()
maria.paga_impuestos()
maria.saludar()
