import random

def mostrar_dni(cola):#devuelve los dni de los integrantes eliminados,
                      #sacando el segundo elemento si el primero es none.
    return [tupla[1] for tupla in cola if tupla[0] is None]

def cola_final(cola):#devuelve los que su segundo elemento no es None
    return [tupla for tupla in cola if tupla[0] is not None]

def creacion_cola():#determina aleatoriamente si el integrante carece de un numero de orden.
    return [((i, random.randint(10000000, 60000000)) if random.choice([True, False]) else (None, random.randint(10000000, 60000000))) for i in range(1, 10)]

# PROGRAMA PRINCIPAL
cola_inicial = creacion_cola()

print("La cola inicial es:", cola_inicial)
print("Los DNI de los integrantes eliminados son:", mostrar_dni(cola_inicial))
print("La cola final es:", cola_final(cola_inicial))