
"""Numero 1"""

"""Dividir las funciones del codigo de manera cohesiva, generando que el cliente pueda comprender facilmente el codigo."""
def calcular_promedio(datos):
    total = sum(datos)
    cantidad = len(datos)
    return total / cantidad




"""Numero 2"""

"""Documentar el codigo con comentarios/docstrings para explicar el funcionamiento de algun detalle que no se puede pasar por alto
   o tambien la explicacion de la funcion en particular"""

def calcular_area_circulo(radio):
    #Calcula el área de un círculo.
    #Retorna:
    #float: El área del círculo.
    return 3.14 * radio**2




"""Numero 3"""

"""Utilizar el manejo de errores y excepciones te da como programador la capacidad de anticipar y gestionar errores de manera explícita donde mejora la claridad del código y facilita el mantenimiento!!!.
   Tratando las excepciones de manera específica, nos puede detallar información detallada sobre el problema, lo que ayuda en la correcion y la comprensión del código.   """
def dividir_numeros(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None

resultado_division = dividir_numeros(10, 0)
if resultado_division is not None:
    print("El resultado de la división es:", resultado_division)
