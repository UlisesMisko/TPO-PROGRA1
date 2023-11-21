import random

def concatenar_colas(cola1, cola2):
    #luego utiliza un while para iterar sobre la cola2. Por cada iteracion, se extrae
    #el primer valor de la cola 2 y se agrega a la cola 1 hasta que la cola 2 quede vacia.
    while cola2:
        elemento = cola2.pop(0)
        cola1.append(elemento)
    return cola1
        

#PROGRAMA PRINCIPAL
cola1 = [random.randint(0, 10) for _ in range(3)]
cola2 = [random.randint(0, 10) for _ in range(4)]

print("Cola 1:", cola1)
print("Cola 2:", cola2)
print("Las colas concatenadas son:", concatenar_colas(cola1, cola2))