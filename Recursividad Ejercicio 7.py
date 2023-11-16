def calcular_mcd(x, y):
    if x == y: 
        return x
    elif x < y: #llama recursivamente intercambiando x e y
        return calcular_mcd(y, x)
    else:
        return calcular_mcd(x - y, y)#llama recursivamente restando y de x y mantiene y constante.

def mcd_recursivo(acumulador, elementos_restantes):
    if not elementos_restantes:
        return acumulador#toma un acumulador inicial
    else:
        return mcd_recursivo(calcular_mcd(acumulador, elementos_restantes[0]), elementos_restantes[1:])
    #y el resto de los elementos en la lista. Utiliza la recursión para calcular el MCD acumulado a través de la lista de elementos.

def main():#programa principal
    numeros = []

    while True:
        try:
            numero = int(input("Ingrese un número entero no negativo (ingrese un valor no entero para finalizar): "))
            if numero < 0:
                print("Por favor, ingrese un número no negativo.")
            else:
                numeros.append(numero)
        except ValueError:
            break  

    if len(numeros) < 2: #verifica si hay al menos dos números
        print("Debe ingresar al menos dos números para calcular el MCD.")
    else:
        resultado_mcd = mcd_recursivo(numeros[0], numeros[1:]) #llama a la función mcd_recursivo con el primer número y
                                                               #el resto de los números en la lista
        print(f"El MCD de {numeros} es: {resultado_mcd}")

if __name__ == "__main__":
    main()





