"""Crear un diccionario que almacene el nombre y las 3 notas de un estudiante. 
Definir una función que calcule la nota promedio y cree un diccionario de salida 
que contenga el nombre del estudiante, su nota promedio y 
regrese una cadena con el nombre y la nota del estudiante. 
"""

def calcula_promedio(notas:dict): promedio = (notas["nota1"]+notas["nota2"]+notas["nota3"])/3 promedio = round(promedio,1) respuesta = { 'notaFinal':promedio, "nombreEstu": notas["nombre"] } return f"La nota final de {respuesta['nombreEstu']} es {respuesta['notaFinal']}" notas = { "nota1":4.5, "nota2":3.5, "nota3":5, "nombre":"Juan" } print(calcula_promedio(notas)) 
