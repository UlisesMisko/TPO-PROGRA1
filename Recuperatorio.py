import random as rd

def menor_stock():
    # Listas con stock bajo
    nombre_bajo, codigo_bajo, stock_bajo = [], [], []

    # Listas temporales para actualizar las listas que se muestran en pantalla
    nuevos_nombres, nuevos_codigos, nuevos_stocks = [], [], []

    for pos in range(len(nombre)):
        if stock[pos] < 5:
            nombre_bajo.append(nombre[pos])
            codigo_bajo.append(codigo[pos])
            stock_bajo.append(stock[pos])
        else:
            nuevos_nombres.append(nombre[pos])
            nuevos_codigos.append(codigo[pos])
            nuevos_stocks.append(stock[pos])

    # Actualiza las listas originales
    nombre[:] = nuevos_nombres
    codigo[:] = nuevos_codigos
    stock[:] = nuevos_stocks

    return nombre_bajo,codigo_bajo,stock_bajo


def muestra(nombre_bajo,codigo_bajo,stock_bajo):
    
    if nombre == []:
        print("\nNo hay modelos con stock disponibles")
        
    else:
        #Listado completo
        print("\nListado completo por Código del producto:")
        for codigos, nombres, stocks in sorted(zip(codigo, nombre, stock)): 
            print(f"Código: {codigos}, Nombre: {nombres}, Stock: {stocks}")
     
        #Modelo con mas Stock
        print("\nEl/Los productos con mayor cantidad de stock:")
        maximo = max(stock)
        for pos,val in enumerate(stock):
            if val == maximo:
                print(f"Modelo {nombre[pos]} con {val} unidades.")
    
        # Productos con la mayor cantidad de stock
        print("\nLos modelos con mayor stock:")
        modelo_stock_tuplas = zip(stock, nombre)
        modelo_stock_ordenado = sorted(modelo_stock_tuplas, reverse=True)
        primeros_elementos = modelo_stock_ordenado[:3]
        for stock_modelo, modelo in primeros_elementos:
            print(f"Modelo {modelo} con {stock_modelo} unidades.")

    #Productos por debajo del stock minimo
    print("\nProductos con stock menor a la minima:")
    for pos,val in enumerate(nombre_bajo):
        print(f"Modelo {val}, codigo:{codigo_bajo[pos]} con {stock_bajo[pos]} unidades")
  
  
def validacion():
    bandera = False
    while not bandera:
        modelo = input("Ingrese nombre del modelo.Presione enter si no desea agregar:")
        
        if modelo == "":
            bandera = True
    
        elif modelo in nombre or modelo.isdigit():
            print("Incorrecto --> Compruebe que el nombre cumpla los siguientes requisitos: \n a)No se permite numeros como nombre \n b)Verificar si se repitio el modelo")
        
        else:
            code = input("Ingrese el codigo del modelo:")
            if code in codigo or len(code) != 4:
                print("Incorrecto --> Compruebe que el codigo cumpla los siguientes requisitos: \n a)Tiene que tener 4 cifras \n b)Verificar si se repitio el codigo")
            elif len(code) == 4:
                nombre.append(modelo)
                codigo.append(code)
                stock.append(rd.randint(0,2))
                print("Su modelo se ha guardado correctamente")
        
nombre = []
codigo = []
stock = []            
            
def main():
    validacion()
    if nombre == []:
        print("No se ha cargado ningun producto. Programa finalizado")
    else:
        n,c,s = menor_stock()
        muestra(n,c,s)
        
if __name__ == "__main__":
    main()

              
      