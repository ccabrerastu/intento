def ejercicio1():
    b = 2400
    ina = 0.0
    acep = 0.4
    merit = 0.6
    i = 1
    while i == 1 : 
        puntuación = float (input("Ingrese la puntuación del usuario: "))     
        if puntuación == ina : 
            pago = 2400 * puntuación
            print ("Su nivel de rendimiento es INACEPTABLE")
            print ("La cantidad de dinero que recibirá es: ", pago , "soles")
        elif puntuación == acep : 
            pago = 2400 * puntuación
            print ("Su nivel de rendimiento es ACEPTABLE")
            print ("La cantidad de dinero que recibirá es: ", pago , "soles")
        elif puntuación >= 0.6 : 
            pago = 2400 * puntuación
            print ("Su nivel de rendimiento es MERITORIO")
            print ("La cantidad de dinero que recibirá es: ", pago , "soles")
        else : 
            print ("La puntuación ingresada no es correcta")
        i = int(input (""" 
            ¿ Dese agregar puntuación de otro empleado ?
            1. Si 
            2. No
            """
            ))

def ejercicio2(): 
    estudiantes = int(input("Ingrese la cantidad total de estudiantes: "))
    a = 0
    b = 0
    promedio = 0
    suma = 0
    mayor = 0
    menor = 0
    # infancia 0 - 2 años
    # niñez 3 - 12 años
    # adolescencia 13 - 17 años
    # juventud 18 - 25 años
    # adultez 26 a más
    while a < estudiantes:
        print("Ingrese edad", a+1)
        edad = int(input("-"))
        if edad >= 0 and edad <= 2 :
            print ("El estudiante se encuentra en la infancia")
        elif edad >= 3 and edad <= 12 : 
            print ("El estudiante se encuentra en la niñez") 
        elif edad >= 13 and edad <= 17 : 
            print ("El estudiante se encuentra en la adolescencia")
        elif edad >= 18 and edad <= 25 :
            print ("El estudiante se encuentra en la juventud")
        else : 
            print ("El estudiante se encuentra en la adultez")
        a = a + 1
        if edad :
            suma = suma + edad
        if edad > mayor:
            mayor = edad
        if b == 0:
            menor = edad
            b = 1
        if edad < menor:
            menor = edad
    promedio = suma / estudiantes
    print (" ---------------------- ")
    print("El promedio total es de :",promedio)
    print("El menor estudiante tiene ",menor," años")
    print("El mayor estudiante tiene ",mayor," años")


def ejercicio3():
    c1 = c2 = c3 = c4 = 0
    op = 1
    while op == 1:
        print("""
        CANDIDATOS A LA ALCALDIA
          ------------------------
        1. Fidel Carita
        2. Joel Chinchazo 
        3. Ivan Málaga
        4. No sabe / No opina
        """
        )
        voto = int (input ("Ingrese el número de su candidato: "))
        if voto == 1:
            c1 = c1 + 1
        elif voto == 2:
            c2 = c2 + 1
        elif voto == 3:
            c3 = c3 + 1
        else : 
            c4 = c4 + 1
        op = int(input("Dese continuar la votacion (1. Si // 2. No) : "))

    print("Los resultados obtenidos son: ")
    print("Fidel Carita    :  " , c1 , "votos")
    print("Joel Chinchazo  :  " , c2 , "votos")
    print("Ivan Málaga     :  " , c3 , "votos")
    print("No sabe / opina :  " , c4 , "votos")

    if c1 > c2 and c1 > c3 and c1 > c4 : 
        print ("El alcade es FIDEL CARITA")
    elif c2 > c1 and c2 > c3 and c2 > c4 : 
        print ("El alcade es JOEL CHINCHAZO")
    elif c3 > c1 and c3 > c2 and c3 > c4 :
        print ("El alcade es IVAN MÁLAGA")
    elif c4 > c1 and c4 > c2 and c4 > c3:
        print ("ELECCIONES NULAS - la mayoría no sabe / no opina")
    elif c1 == c2 or c2 == c1 :
        print ("Hay segunda vuelta entre FIDEL CARITA Y JOEL CHINCHAZO")
    elif c1 == c3 or c3 == c1:
        print ("Hay segunda vuelta entre FIDEL CARITA E IVAN MALAGA")
    elif c2 == c3 or c3 == c2:
        print ("Hay segunda vuelta entre IVAN MALAGA Y JOEL CHINCHAZO")
    else :
        print ("Nadie ocupó el primer lugar")
