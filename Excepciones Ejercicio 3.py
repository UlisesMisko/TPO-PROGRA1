def mes(num):
        try:
            meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
 
            if num < 1 and num > 12:#valida que el numero de mes este entre 1 y 12
                raise ValueError 
            else:
                nombre=meses[num-1] #-1 porque arranca desde 0
        except (ValueError,TypeError,IndexError):
            nombre='' #Si hay un error devuelve un espacio en blanco
        return nombre

#Si el numero pasado como parametro no es valido (en este caso > de 1 y < de 12) se fuerza una excepcion

num = 10
nombre=mes(num)
print(nombre)