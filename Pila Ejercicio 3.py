
def desapilar_y_tope(pila):
    if not pila_vacia(pila):#La pila esta vacia?
        pila.pop()#desapila elemento superior
        return pila[-1]#retorna el nuevo tope
    else:
        return ("La pila esta vacia")    

def pila_vacia(pila):
    return len(pila) == 0 #devuelve True si la pila esta vacia, False si no

def ordenar_pila(pila): #Ordena la pila (ascendente) con el metodo de seleccion
    n = len(pila)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if pila[j] < pila[min_index]:
                min_index = j
        pila[i], pila[min_index] = pila[min_index], pila[i]
    return pila #retorna pila ordenada de menor a mayor

#PROGRAMA PRINCIPAL
def inicializar_pila():
    pila = []
    while True:
        numero = int(input("Ingrese el numero que desea agregar(Ingrese -1 para terminar de cargar datos): "))
        if numero == -1:
            break
        else:
            pila.append(numero)
    return pila

mi_pila = inicializar_pila()
print("Pila original:", mi_pila)

pila_ordenada = ordenar_pila(mi_pila.copy())
print("La pila ordenada es: ", pila_ordenada)

desapilar_y_tope(mi_pila)
print("La pila despues de desapilar y su valor en el tope es:", mi_pila)


