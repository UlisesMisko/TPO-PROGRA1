import random as rd

def menor_stock():
    nombre_bajo = []
    codigo_bajo = []
    stock_bajo = []
    indices_a_eliminar = []
    
    for pos,val in enumerate(nombre):
        if stock[pos] < 5:
            nombre_bajo.append(nombre[pos])
            codigo_bajo.append(codigo[pos])
            stock_bajo.append(stock[pos])
            indices_a_eliminar.append(pos)
    
    # Eliminar elementos de las listas originales en orden inverso para evitar desplazamiento de índices
    for idx in reversed(indices_a_eliminar): 
        nombre.pop(idx)
        codigo.pop(idx)
        stock.pop(idx)    
    
    return nombre_bajo,codigo_bajo,stock_bajo

                            
def muestra(nombre_bajo,codigo_bajo,stock_bajo):
    
    #Listado completo
    print("\nListado completo por Código del producto:")
    for codigos, nombres, stocks in sorted(zip(codigo, nombre, stock)): 
        print(f"Código: {codigos}, Nombre: {nombres}, Stock: {stocks}")
    
    #Productos por debajo del stock minimo
    print("\nProductos con stock menor a la minima:")
    for pos,val in enumerate(nombre_bajo):
        print(f"Modelo {val}, codigo:{codigo_bajo[pos]} con {stock_bajo[pos]} unidades")
        
    #Modelo con mas Stock
    print("\nEl/Los productos con mayor cantidad de stock:")
    if stock:
        maximo = max(stock)
        for pos,val in enumerate(stock):
            if val == maximo:
                print(f"Modelo {nombre[pos]} con {val} unidades.")
    else:
        print("\nNo hay modelos con stock disponible.")
        
    
    #Productos con la mayor cantidad de stock
    print("\nLos 3 modelos con mayor stock:")
    modelo_stock_tuplas = zip(nombre, stock)
    modelo_stock_ordenado = sorted(modelo_stock_tuplas, key=lambda x: x[1], reverse=True) 
    primeros_tres_elementos = modelo_stock_ordenado[:3]
    for modelo, stock_modelo in primeros_tres_elementos:
        print(f"Modelo {modelo} con {stock_modelo} unidades.")
   
   
def validacion():
    bandera = False
    while not bandera:
        modelo = input("Ingrese nombre del modelo.Presione enter si no desea agregar:")
        if modelo == "":
            bandera = True
        elif modelo in nombre or modelo.isdigit():
            print("Incorrecto --> Verifique los siguientes requisitos: \n a)No se permite numeros como nombre \n b)Verificar si se repitio el modelo")
        else:
            code = input("Ingrese el codigo del modelo:")
            if code in codigo or len(code) != 4:
                print("Incorrecto --> Verifique los siguientes requisitos: \n a)Tiene que tener 4 cifras \n b)Verificar si se repitio el codigo")
            elif len(code) == 4:
                nombre.append(modelo)
                codigo.append(code)
                stock.append(rd.randint(0,10))
                print("Su modelo se ha guardado correctamente")

#main:
nombre = []
codigo = []
stock = []
validacion()
n,c,s = menor_stock()
muestra(n,c,s)
              
      
            
