def binario_a_decimal(binario, posicion=0): #Toma como argumento el numero binario y la posicion actual
    if binario == 0:
        return 0
    else:
        return (binario % 10) * (2 ** posicion) + binario_a_decimal(binario // 10, posicion + 1)
        #si divide el numero por 10 en cada llamada para avanzar a la siguiente posicion
        #el resultado se calcula sumando el ultimo digito multiplicado por 2 elevado a la posicion actual
        #la funcion se llama a si misma de manera recursiva

#Programa principal
numero_binario = int(input("Ingrese un numero binario: "))
resultado_decimal = binario_a_decimal(numero_binario)
print(f"El número binario {numero_binario} es igual a {resultado_decimal} en decimal.")