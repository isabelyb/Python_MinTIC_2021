"""22. Verificar si un texto que termina en punto es un palíndromo (capicúa). Un texto es
palíndromo si se lee lo mismo de izquierda a derecha o de derecha a izquierda. Ej: “Amor
a roma”
"""

def main():
    palindrome()


def palindrome():
    texto = input("Ingrese una frase terminada en punto, para verificar si es palíndrome: ")
    texto_limpio = texto.replace(" ", "")
    palabra_lista = texto_limpio.replace(".", "")
    palabra = palabra_lista.lower()
    palabra_invertida = palabra[::-1]
    
    if palabra == palabra_invertida:
        print("Es palíndrome")
    else:
        print("No es palíndrome")
    

if __name__ == '__main__':
    main()