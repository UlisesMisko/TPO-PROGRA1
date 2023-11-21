import random

def creacion(f,c): #Crea la matriz
    matriz = [ [0]*c for i in range(f)]
    return matriz

def carga(matriz): #Carga los valores 
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = random.randint(1,100)

def muestra(matriz): #Muestra en pantalla la matriz
    for fila in matriz:
        for elemento in fila:
            print("%4d" %elemento, end = "")
        print()

def suma_matriz_recursiva(matriz, fila, columna):#Hace la suma de los elementos de manera recursiva
    if fila == len(matriz):
        return 0
    if columna == len(matriz[0]):
        return suma_matriz_recursiva(matriz, fila + 1, 0)
    return matriz[fila][columna] + suma_matriz_recursiva(matriz, fila, columna + 1)

def main(): #Pide al usuario tamaño de la matriz y llama a las funciones
    marcador = False
    while not marcador:
        a = int(input("Ingrese el numero de filas:" ))
        b = int(input("Ingrese el numero de columnas:" ))
        if a>0 and b>0:
            marcador = True
    x = creacion(a,b)
    carga(x)
    muestra(x)
    suma_total = suma_matriz_recursiva(x, 0, 0)#Suma del primer elemento con el que lo sucede, hasta que termine la matriz
    print(f"La suma total de los elementos de la matriz es: {suma_total}")

if __name__ == "__main__":
    main()
    