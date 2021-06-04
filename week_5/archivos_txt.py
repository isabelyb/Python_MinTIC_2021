# ciudades =['Maicao', 'Meta', 'Leticia', 'Medellín']

# a = open('/home/isa/Documents/MinTIC/Python_MinTIC/week_5/archivo_txt.txt', 'r')

# for i in ciudades:
#     a.write(i)
#     a.write('\n')

# a.close()

# print(list(a))

'''
# Abre el archivo para escribir y elimina los archivos anteriores si existen
fic = open("Archivos/text.txt", "w")

# Abre el archivo para agregar contenido
fic = open("Archivos/text.txt", "a")

# Abre el archivo en modo lectura
fic = open("Archivos/text.txt", "r")

fic.close()
'''

data = ["Línea 1", "Línea 2", "Línea 3", "Línea 4", "Línea 5"]

#Escribir archivos de texto en Python
fic = open("text_1.txt", "w")

for line in data:
    fic.write(line)
    fic.write("\n")
    
fic.close()

#Escribir el archivo línea a línea¶
fic = open("text_2.txt", "w")

for line in data:
    print(line, file=fic)
    
fic.close()

#Escribir el archivo de una vez
fic = open("text_3.txt", "w")
fic.writelines("%s\n" % s for s in data)
fic.close()

#Leer archivos de texto en Python

fic = open('text_1.txt', "r")
lines = fic.readlines()
print(lines)
fic.close()

fic = open('text_1.txt', "r")
lines = list(fic)
print(lines)
fic.close()

#Leer el archivo línea a línea

fic = open('text_1.txt', "r")
lines = []

for line in fic:
    lines.append(line)
print(lines)

fic.close()

#Eliminar los saltos de línea en el archivo importado

lines1 = [s.rstrip('\n') for s in lines]
print(lines1)