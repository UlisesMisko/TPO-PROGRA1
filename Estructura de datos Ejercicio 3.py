def tupla(mail):#Divide el mail en partes y devuelve cada una de sus partes separadas
    partes1 = mail.split('@')
    partes2 = partes1[1].split('.')
    resultado = (partes1[0], *partes2)
    return resultado
            
def main():#Verifica que el mail ingresado sea valido
    bandera = False
    while not bandera:
        mail = input("Ingrese una dirección de correo:  ")
        if "@" not in mail or "." not in mail:
            print("Por favor, ingrese una dirección de correo válida que contenga '@' y '.'.")
        else:
            bandera = True
            
    resultado_tupla = tupla(mail)
    print(resultado_tupla)


if __name__ == "__main__":
    main()
