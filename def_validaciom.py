def validacion():
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


def archivoo():   # Se encarga de abrir el archivo, si es que existe.
    fechas, eq_loc, eq_vis, eq_marcador = [], [], [], []
    
    try:
        x = input("Ingrese nombre del archivo: ")
        archivo = open(x, 'r', encoding='utf-8')
        
        for linea in archivo:
            columnas = linea.strip().split(',')
            fechas.append(columnas[0])
            eq_loc.append(columnas[1])
            eq_vis.append(columnas[2])
            eq_marcador.append(columnas[3])
                             
        return fechas, eq_loc, eq_vis, eq_marcador
        
    except IOError:
        print("Archivo no encontrado. El archivo de texto tiene que estar en la misma carpeta que el programa.")
    finally:
        archivo.close()    



