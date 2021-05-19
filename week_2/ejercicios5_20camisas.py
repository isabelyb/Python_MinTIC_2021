"""20. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran
tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son
menos de tres camisas un descuento del 10%
"""

def main():
    pagar()


def pagar():
    precio_camisa = 20000
    camisas = int(input("Cuantas camisas va a comprar?  "))
    precio_regular = camisas * precio_camisa
    pagar = ""

    if camisas >= 3:
        pagar = precio_regular - ((precio_regular*20)/100)
    else:
        pagar = precio_regular - ((precio_regular*10)/100)

    print(f"El precio por comprar {camisas} camisas es: {pagar} pesos")



if __name__ == '__main__':
    main()