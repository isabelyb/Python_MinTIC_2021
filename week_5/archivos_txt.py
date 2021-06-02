# ciudades =['Maicao', 'Meta', 'Leticia', 'Medellín']

# a = open('/home/isa/Documents/MinTIC/Python_MinTIC/week_5/archivo_txt.txt', 'r')

# for i in ciudades:
#     a.write(i)
#     a.write('\n')

# a.close()

# print(list(a))



# w = write
# r = read
# a = add

#abriendo archivos txt

#para leer r, escribir w (borra lo que tiene y escribe datos), añadir a (añade datos en la ultima linea)
a = (open("C:/1. AYDA/6. UTP/Unidad5/datos.txt", "r"))   
print (list(a))
a.close         # siempre que se hace un open se deb cerrar con un close

#AÑADIENDO CODIGO AL ARCHIVO
lista1 = ["ecuador", "peru", "Brasil", "Mexico"]
b = (open("C:/1. AYDA/6. UTP/Unidad5/datos.txt", "a"))   # AÑADIENDO SIN BORRAR   
for i in lista1:
    b.write(i)
    b.write("\n")
b.close 


'lista1 = ['Maicao','Meta', 'Leticia', 'Medellin']
a = open('ciudadesP65.txt', 'w') #r: lectura, w: escritura y a:añadir
for i in lista1:
    a.write(i)
    a.write('\n')
a.close()
b = open('ciudadesP65.txt','r')
lista1 = list(b)
print(lista1)
lista2 = [x.rstrip('\n') for x in lista1]
print(lista2)
b.close()