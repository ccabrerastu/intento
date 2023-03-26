def ejercicio1():
    #Elaborar un programa principal que llame a funciones mediante un menú de opciones
    #para realizar lo siguiente: cambiar el formato de las palabras de mayúsculas a
    #minúsculas, otra función que nos señale cuántos caracteres tiene la palabra ingresada
    #y que la muestre al revés. La cadena se pasa como parámetro a cada función requerida.
        print("MENÚ DE OPCIONES: ")
        (print(''' 
        1. Transformación de mayusculas a minusculas
        2. Contador de caracteres y palabra al revés
        ''')) 
        alternativa = int(input("Ingrese una alternativa: "))
        def op1():
            p = str(input("Ingrese una palabra: "))
            mayuscula = p.lower()
            print(mayuscula)
        def op2():
            p = str(input("Ingrese una palabra: "))
            cant = p.__len__()
            print(cant)
            txt = ""
            for letra in p:
                txt = letra + txt
            print(txt)
        if alternativa ==1:
            op1()
        else:
            op2()
#ejercicio1()

def ejercicio2():
    #Escribir una función que determine el signo zodiacal de una persona y su edad a
    #partir de la fecha de nacimiento. 
    (print("Ingrese el nº de mes: "))
    mes = int(input("""
        1 - Enero
        2 - Febrero
        3 - Marzo
        4 - Abril
        5 - Mayo
        6 - Junio
        7 - Julio
        8 - Agosto
        9 - Setiembre
        10 - Octubre
        11 - Noviembre 
        12 - Diciembre
        """) ) 
    signo=""
    if mes==1:
            signo="Capricornio"
    elif mes==2:
            signo="Acuario"
    elif mes==3:
            signo="Piscis"
    elif mes==4:
            signo="Aries"
    elif mes==5:
            signo="Tauro"
    elif mes==6:
            signo="Géminis"
    elif mes==7:
           signo="Leo"
    elif mes==8:
           signo="Virgo"
    elif mes==9:
           signo="Libra"
    elif mes==10:
           signo="Libra"
    elif mes==11:
           signo="Escorpio"
    else:
           signo="Sagitario"
    print("Su signo zodiacal es: ", signo)
#ejercicio2()