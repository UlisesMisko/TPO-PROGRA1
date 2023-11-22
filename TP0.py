from def_validacion import validacion
from def_validacion import archivoo

def cant_goles(archivo):#Muestra los 3 equipos con mayores goles
    lista = [columna[3] for columna in archivo]
    lista2 = []
        
    for elemento in lista:
        x = lista.count(elemento)
        tuplaA = (x,elemento)      
        if tuplaA not in lista2:
            lista2.append(tuplaA)
    lista2.sort(reverse=True)
    
    equipos_lst = [tupla[1] for tupla in lista2[:3]]
        
    return lista2, archivo, equipos_lst

    
def dif_gol(archivo, equipos_lst):     #Mostrar las diferencias de goles DE TODAS las fechas para aquellos 3 equipos que tengan mas goles en todas las fechas FIFA.
    resultados_por_equipo = {equipo: {} for equipo in equipos_lst}

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
   
        
def lectura(lista):                          

    lista2,archivos,equipos_lst = cant_goles(lista)
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

def main():
    validacion()
    lista = archivoo()
    lectura(lista)

main()
