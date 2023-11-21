def contarvocales(palabra):#contar las vocales de cada palabra
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    #Lo vimos con Thompson el uso del replace, pero no me funciona.
    palabra = palabra.replace(',', '').replace('.', '') #reemplaza las comas y puntos por espacios vacios

    for letra in palabra:#itera sobre cada letra y al encontrar una vocal la suma en el diccionario
        if letra.lower() in conteo_vocales:
            conteo_vocales[letra.lower()] += 1
    return conteo_vocales


def main():  
    frase = input("Ingrese una frase: ") #solicita por teclado el ingreso de una frase
    total_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    palabras = frase.split() #divide la frase en palabras
    for palabra in palabras:
        resultado = contarvocales(palabra) #llama a la funcion creada
        for vocal in total_vocales:
            total_vocales[vocal] += resultado[vocal]

        print(f'Word: {palabra} \n{resultado} \n') #devuelve el conteo total de las vocales
    print(f'Conteo total de vocales:  {total_vocales}')

if __name__ == "__main__":
    main()