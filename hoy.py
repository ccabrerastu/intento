def operaciones(a,b):
    suma=a+b
    resta=a-b
    multiplica=a*b
    division=a/b
    return(suma,resta,multiplica.division)

def main():
    num1=int(input("Ingrese un numero entero: "))
    num2=int(input("Ingrese otro numero entero: "))

    ar,br,cr,dr=operaciones(num1, num2)
    
    print("El valor de la suma es: ",ar)
    print("El valor de la resta es: ",br)
    print("El valor de la multiplicacion es: ",cr)
    print("El valor de la division es: ",dr)
#main()

usuario1="Alvaro"
clave1="123"
admin="Ana"
clave2="000"

def logeo(ingreso):
    usuario=input("Ingrese su usuario: ")
    clave=input("Ingrese su clave: ")
    ingreso=ingreso+1
    return(usuario,clave,ingreso)

def comparacion(usuario,clave,ingreso):
    if (usuario==usuario1 and clave==clave1) or (usuario==admin and clave==clave2) :
        print("Bienvenido al sistema")
    else: 
        print("Usuario o contraseña estan incorrectos!! ")
        if ingreso==3:
            print("Usted ha llegado al limite de intentos")

def main():
    ingreso=0
    while ingreso<3:
        usuario,clave,ingreso=logeo(ingreso)
        acceso=comparacion(usuario,clave,ingreso)
#main()

# Escribir una funcion en la cual vamos a unir dos cadenas
# que seran requeridas en dos funciones una nombre y la otra profesion
# y lo vamos a unir en una funcion principal, la cual debe ejecutar
# la union de nombres hasta cuando el usuario ingrese una flag.


def nombre():
    a=str(input("Ingrese un nombre: "))
    return a

def profesion():
    b=str(input("Ingrese una profesion: "))
    return b


def union(): 
    i=1
    while i==1:
        print(nombre(),profesion())
        i=int(input("Desea agregar otros datos? 1=SI 0=NO"))
#union()


# vamos a realizar el pequeño juego de a adivinar un numero. Lo tendremos 
# puesto en una variavle el valor que nosotros queramos. El numero sera 
# entre 1 y 100
# Tendremos que hacer los siguientes subprocesos: 
# leerNumero(): Pide un numero y hasta que el usuario no escribe un valor
# entre 1 y 100, vuelve a pedir el valor.
# comprobarValor(numeroUsuario, numeroCorrecto): comprueba si el 
# numero es correcto. Da un resultado de salida en la funcion principal.


def leernumero():
    i=1
    while i==1:
        n=int(input("Ingrese un numero del 1 al 100: "))
        if n>=1 and n<=100:
            i=0
        else:
            print("El numero no es valido, ingrese otro")
            print(" ")

    return n

def comprobarvalor(numeroUsuario, numeroCorrecto):
    if numeroUsuario==numeroCorrecto:
        i=True  
    else:
        print("Numero incorrecto ")
        print(" ")
        i=False
    return i


def juego():
    import random
    aleatorio= random.randint(1, 100)
    print (aleatorio)

    respuesta=False
    while respuesta==False:
        numero=leernumero()
        respuesta=comprobarvalor(numero,aleatorio)

    print("Felicidades!, el numero correcto es: ", numero)

juego()
