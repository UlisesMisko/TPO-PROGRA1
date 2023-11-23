def grabararchivo(arch,registro):
  try:
    arch = open(arch, "at")
    arch.write(str(registro))
  except IOError:
    print("No se pudo crear el archivo")


#Programa principal
try:
  arch = open(r"nacionalidad.txt", "rt")
  for registro in arch: 
    apellido, nombre = registro.split(",")
    if apellido[-3:] == "ian":
      grabararchivo("Armenia.txt", registro)
    elif apellido[-3:] == "ini":
      grabararchivo("Italia.txt", registro)
    elif apellido[-2:] == "ez":
      grabararchivo("España.txt", registro)
    else:
      print("Se descarta el apellido no correspondiente:",apellido)
except IOError:
  print("No se pudo leer el archivo")
finally:
  arch.close()
  print("Se ejecuto el programa")

#Se abre el archivo y se lee cada registro, si no se puede abrir ocurre la excepcion y se cierra con el finally
#Se hace el split para tomar solo el apellido y evaluar las ultimas letras del apellido,
#Si coincide con lo evaluado, se graba el archivo correspondiente