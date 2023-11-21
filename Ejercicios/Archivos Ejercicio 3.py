def grabarrangoalturas(registro):
  try:
    arch = open(r"alturas.txt", "at")
    arch.write(str(registro)+ "\n")
  except IOError:
    print("No se pudo crear el archivo")
  finally:
    arch.close()

def grabarpromedio(registro):
  try:
    arch = open(r"promedio.txt", "at")
    arch.write(str(registro)+ "\n")
  except IOError:
    print("No se pudo crear el archivo")
  finally:
    arch.close()

# En el programa principal, se carga por teclado los deportes y las alturas. Corta la carga con un valor -1, tanto los
# deportes como las alturas 
# todos los valores se graban en un archivo alturas para ello, se utiliza la funcion grabarrangoalturas pasando como parametro 
#los deporte y las alturas segun correponda 
 

#Programa principal
promediogeneral = 0

while True:
  deporte = str(input("Ingrese un deporte (-1 para finalizar):"))
  if deporte == "-1":
    break
  else:
    grabarrangoalturas(deporte)
    while True:
      altura = float(input("Ingrese una altura (-1 para finalizar):"))
      if altura == -1:
        break
      else:
        grabarrangoalturas(altura)

#abre el archivo alturas grabado en el paso anterior. lo lee analizando cada registro.
# graba un nuevo arhivo con los promedios por cada disciplica ultilizando la funcion 
#grabarpromedio. calcula el promedio general de todas las alturas 

try:
  arch = open(r"alturas.txt", "rt")
  lineas = arch.readlines()

  cantidad = 0
  suma = 0
  cantdep = 0
  deporte_anterior = ''
  for linea in lineas:
    try:
      altura = float(linea)
    except:
      deporte = linea
      cantdep += 1
    else:
      cantidad += 1
      suma += altura

    if deporte != deporte_anterior:
      if cantidad > 1:
        promedio = suma / cantidad
        grabarpromedio(deporte_anterior)
        grabarpromedio(promedio)
        promediogeneral += promedio
      deporte_anterior = deporte
      cantidad = 0
      suma = 0

  promedio = suma / cantidad
  promediogeneral += promedio
  grabarpromedio(deporte_anterior)
  grabarpromedio(promedio)

  print("El promedio general es: ", promediogeneral / cantdep)

except IOError:
  print("No se pudo abrir el archivo")
finally:
  arch.close()