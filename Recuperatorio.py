import random as rd


def menor_stock(nombre,codigo,stock):
    nombre_bajo = []
    codigo_bajo = []
    stock_bajo = []
    for pos,val in enumerate (nombre):
        if stock[pos] < 5:
            val.append(nombre_bajo)
            codigo[pos].append()
            
            


    


def ordenamiento(nombre,codigo,stock): #Ordena de menor a mayor por codigo
    for codigos, nombres, stocks in sorted(zip(codigo, nombre, stock)):
        


    
def muestra(nombre,codigo,stock):
    print("\nListado completo por Código del producto:")
    for codigos, nombres, stocks in sorted(zip(codigo, nombre, stock)):
        print(f"Código: {codigo}, Nombre: {nombre}, Stock: {stock}")
   
   
   
   

def validacion():
    nombre = []
    codigo = []
    stock = []
    bandera = False
    while not bandera:
        modelo = input("Ingrese nombre del modelo.Presione enter si no desea agregar.")
        if modelo == "":
            bandera = True
        elif modelo in nombre or modelo.isdigit():
            print("Verifique los siguientes requisitos: \n a)No se permite numeros como nombre \n b)Verificar si se repitio el modelo")
        else:
            code = input("Ingrese el codigo del modelo. --> Tiene que tener 4 cifras <--  ")
            if code in codigo or len(code) != 4:
                print("Incorrecto. Revise el codigo distinto de 4 cifras")
            elif len(code) == 4:
                nombre.append(modelo)
                codigo.append(code)
                stock.append(rd.randint(0,10))
                print("Su modelo se ha guardado correctamente")
                
    return nombre,codigo,stock
    
    
def main():      
    x,y,z = validacion()
    ordenamiento(x,y,z)
              
      
            