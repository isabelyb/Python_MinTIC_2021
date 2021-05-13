notas = {
    "nota1":4.5,
    "nota2":3.5,
    "nota3":5,
    "nombre":"Juan"
    } 
print(notas) 

frutas = dict(
    manzana = 5000, banana = 2500, lulo =4000, pera=5500) 
print(frutas) 
print(frutas["manzana"]) 

print(notas["nota3"]) 
frutas.clear() 
print(frutas) 
notasCopia = notas.copy() 
print(notasCopia) 
print(notas==notasCopia) 

for nota in notas:
    print()