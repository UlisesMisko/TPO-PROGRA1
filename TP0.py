def cant_goles(archivo):      #Muestra los 3 equipos con mayores goles
    lista = []
    lista2 = []
    for columna in archivo:
        lista.append(columna[3])
        
    for elemento in lista:
        x = lista.count(elemento)
        tuplaA = (x,elemento)      
        if tuplaA not in lista2:
            lista2.append(tuplaA)
    lista2.sort(reverse=True)
    
    equipos_lst = []
    for tupla in lista2[:3]:
        equipos_lst.append(tupla[1])
        
    return lista2, archivo, equipos_lst


def dif_gol(archivo, equipos_lst):     #Mostrar las diferencias de goles DE TODAS las fechas para aquellos 3 equipos que tengan mas goles en todas las fechas FIFA.
    resultados_por_equipo = {equipo: {} for equipo in equipos_lst}        """Uso diccionario por comprension y ademas agrego otro diccionario dentro para manejar de manera mas eficiente los valores
                                                                             ya que dentro de cada equipo tengo un diccionario con las claves que son las fechas y el resultado que son la diferencia de goles en cada fecha
                                                                             Esto fue uno de los temas que mas tuve que investigar por mi propia cuenta. Solicito si es posible una aclaracion.""" 
    for columnas in archivo:
        fecha, eq_loc, eq_vis, eq_marcador = columnas[:4]       
             
        for equipo in equipos_lst:
            if equipo in [eq_loc, eq_vis]:                
                if fecha not in resultados_por_equipo[equipo]:
                    resultados_por_equipo[equipo][fecha] = 0
                if eq_marcador == equipo:
                    resultados_por_equipo[equipo][fecha] += 1 
                else:
                    resultados_por_equipo[equipo][fecha] -= 1
                    
    return resultados_por_equipo

    
def max_dif(resultados_por_equipo):   #Detectar el equipo (de los 3) con la maxima cantidad diferencia de gol en un partido.
    max_dif_equipo, max_dif = [], 0   

    for equipo, resultados in resultados_por_equipo.items():
        for fecha, dif in resultados.items():
            if dif > max_dif:
                max_dif = dif
                max_dif_equipo = [equipo]
            elif dif == max_dif:
                max_dif_equipo.append(equipo)
                
    return max_dif_equipo, max_dif   
   
      
      
      
      
      
def lectura():   #Se encarga de abrir el archivo, si es que existe.
    lista = []                                                      """Guardo todo en memoria ---> MAL"""                                                                      
    try:                                                               #Arreglarlo
        x = input("Ingrese nombre del archivo")
        archivo = open(x,'r',encoding='utf-8')
        
        for linea in archivo:
            lista.append(linea.strip().split(','))                     
        return lista
        
    except IOError:
        print("Archivo no encontrado")
    finally:
            archivo.close()    
        

def validacion():  #Acceso al programa            """Esta funcion la entendi como el ultimo enunciado del TPO en donde con otro grupo nos creamos la misma funcion con los mismos datos para acceder al archivo del cliente"""
    usuario = "InnovaCode"
    contraseña = "CodingCorporation"
    bandera = False
    while not bandera:
        usuario_ingresado = input("Ingrese el nombre de usuario: ")
        contraseña_ingresada = input("Ingrese la contraseña: ")

        if usuario == usuario_ingresado and contraseña == contraseña_ingresada:
            print("Acceso permitido")
            print("A continuacion, deberá ingresar el nombre del archivo. Recuerde que si es un archivo de texto coloque al final del nombre .txt")
            bandera = True
        else: 
            print("Acceso denegado, contraseña o usuarios incorrectos")
    main()
    
    
def main():                          
    archivo = lectura()
    
    lista2,archivos,equipos_lst = cant_goles(archivo)
    print("Los equipos con mayor cantidad de goles son:")
    for pos,val in enumerate(lista2[:3],1):
        print(f"{pos}° {val[1]} con {val[0]} goles.")
           
    resultados_por_equipo = dif_gol(archivos,equipos_lst)
    for equipo, resultados in resultados_por_equipo.items():
        print(f"\nEquipo {equipo}:")
        for fecha, dif_goles in resultados.items():
            print(f"Fecha: {fecha}. Diferencia de goles = {dif_goles}")
    
    max_dif_equipo,max_diff = max_dif(resultados_por_equipo)
    if len(max_dif_equipo) == 1:
        print(f"El equipo {max_dif_equipo[0]} tiene la mayor diferencia de goles en un solo partido con {max_diff} goles")
    else:
        equipos_str = ', '.join(max_dif_equipo)
        print(f"Hay un empate entre los equipos {equipos_str} con la mayor diferencia de goles en un solo partido: {max_diff} goles")


validacion()


