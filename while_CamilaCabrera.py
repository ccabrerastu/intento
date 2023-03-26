def ejercicio1():
    suma = 0
    mult = 1
    i = 1
    while i != 0:
        i = float(input("Introducir un numero: "))
        suma = suma + i 
        resta = resta - i 
        mult = mult * i
        # i = int(input("Desea ingresar otro numero? 1. Si // 2. No"))
    print("El resultado de la suma es: ", suma)
    print("El resultado de la resta es: ", resta)
    print("El resultado de la multiplicación es: ", mult)


def ejercicio2():
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
    else :
        print ("Nadie ocupó el primer lugar")



def ejercicio3(): 
    intento = 0
    usuario = "Camila"
    contraseña = 123
    while intento <= 3 : 
        usuarioin = input ("Ingrese el usuario: ")
        contraseñain = int(input("Ingrese la contraseña: "))
        intento = intento + 1
        if usuarioin == usuario and contraseñain == contraseña :
            print ("¡Bienvenido al sistema!")
            intento = 5
        else : 
            print ("Usuario o contraseña incorrectos, intente otra vez")
        if intento == 4 : 
            print ("Usted ha excedido los intentos permitidos")

def ejercicio4(): 
    a = 0
    i = 1
    n_notas = int(input("Ingrese el numero de notas: "))
    total_n = 0
    while i == 1:
        student=input("Ingrese el nombre del estudiante: ")
        while a < n_notas: 
            nota = float(input("Ingrese la nota: "))
            total_n = total_n + nota
            a = a + 1
            prom = total_n / 3
        print("El promedio del estudiante es: ", prom)
    i=int(input("¿Desea continuar el registro de notas? 1.Si // 2. No)"))   


def ejercicio5():
    total = 0
    i = 1
    saldo = float(input("Ingrese su saldo: "))
    while i == 1: 
        op =str(input("""
        ¿Desea depositar dinero o retirar dinero? 
        D - Deposito 
        R - Retiro
        """
        ))
        monto=float(input("Ingrese el monto a depositar: "))
        if op=="D" or op=="d":
            saldo=saldo+monto
            print("Su nuevo saldo es: ",saldo)
        elif op=="R" or op=="r":
            saldo=saldo-monto
            if saldo<0:
                print("Saldo insuficiente")
            elif saldo>=0:
                print("Su nuevo saldo es: ", saldo)
        
        opcion=""

        i=int(input("""
        ¿Desea realizar otra transaccion? 
        1. Si
        2. No
        """
        ))
