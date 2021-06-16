#encapsulamiento
#ocultamos atributo y métodos (__)
#métodos getters ->>obtener
#métodos setter ->> fijar

class circulo:
    __pi = 3.141592
    def __init__(self, y):
        self.__radio = y
    
    def __cuadrado(self,x):
        return x**2
    def area(self):
        return circulo.__pi*(self.__cuadrado(self.__radio))
    #getter
    def getRadio(self):
        return self.__radio
    #setter
    def setRadio(self,nuevoRadio):
        self.__radio = nuevoRadio

circulo1 = circulo(2) #instanciar
print(circulo1.area())
print(circulo1.getRadio())
#print(circulo1._circulo__radio)
circulo1.setRadio(5)
print(circulo1.getRadio())
print(circulo1.area())