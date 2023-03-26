#nombre="erbert"
#print(max(nombre))
#print(min(nombre))

def operaciones(a,b):
    suma=a+b
    resta=a-b
    mult = a*b
    div = a/b
    return(suma,resta,mult, div)

def main():
    n1 = int(input("Ingrese un valor entero: "))
    n2 = int(input("Ingrese otro valor entero: "))
    ar,br,cr,dr=operaciones(n1,n2)
    print("La suma es: ", ar)
    print("La resta es: ", br)
    print("La multiplicacion es: ", cr)
    print("La division es: ", dr)

#main()

user="Lili"
clave1="123"
admin="Ana"
clavead="000"

def logeo(ingreso):
    usuario=input("Ingrese su usuario: ")
    clave=input("Ingrese su clave: ")
    ingreso = ingreso + 1
    return(usuario,clave,ingreso)

def comparacion(usuario,clave, ingreso):
    if (usuario==user and clave==clave1) or (usuario==admin and clave==clavead): 
        print("Bienvenido")
    else: 
        print("Usuario o contraseña incorrecta.")
        if ingreso==3:
            print("Ha llegado al límite de intentos")
        
def main():
    ingreso=0 
    while ingreso<3:
        usuario,clave,ingreso=logeo(ingreso)
        comparacion(usuario,clave,ingreso)
#main()

def names():
        nombre = str(input("Ingrese un nombre: "))
        return nombre

def prof():
        profesion = str(input("Ingrese su profesión: "))
        return profesion

def conexion():
    op = 1
    while op==1:
        print("La unión es", names(), prof())
        op=int(input("Agregar más datos ? (1. Si/ 0.No): "))
#conexion()


#ejercicio 2. Vamos a realizar el pequeño juego de adivinar un número. Lo tendremos
# puesto en una variable el valor que nosotros queramos. El numero será
# entre 1 y 100.
# Tendremos que hacer los siguientes subprocesos:
# leerNumero(): Pide un número y hasta que el usuario no escribe un valor
# entre 1 y 100, vuelve a pedir el valor.
# comprobarValor(numeroUsuario, numeroCorrecto): comprueba si el
# numero es correcto.Da un resultado de salida en la funciòn principal


def leernum():
    import random
    numero = random.randint(1,100)
    n = int(input("Ingrese un numero entre 1 al 100: "))
    if n < 1 or n > 100 : 
        n=int(input("Vuelva a ingresar el número entre 1 al 100: "))
    return (n,numero)

def comprobarvalor(n,numero):
    if n == numero: 
        print("Número acertado")
    else: 
        print("Ud ingresó: ", leernum())
        print ("El  número a adivinar era" , numero)

    


