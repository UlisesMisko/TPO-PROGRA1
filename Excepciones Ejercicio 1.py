def numero ():
    while True: 
        try:
            nro = int(input("Ingrese un numero: "))
            if nro <= 0:
                print("El numero debe ser mayor a 0")
            else:
                print(f"El valor ingresado es {nro}")
                break
        except (ValueError,TypeError):
            print("Error ingrese un numero que este dentro de los naturales")

#Ingresar un numero por teclado hasta que este sea natural, cuando eso pasa se imprime.
#Si se ingresa un valor que no sea entero, se activa la excepcion

#Programa principal
numero()