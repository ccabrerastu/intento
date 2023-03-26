def dihola():                     #la función retorna "hello".
    print("Hello!")
#dihola()

#------------------------------------------------------

def holaconnombre(name):            #la función recibe un argumento                                   
    print("Hello" , name  + "!")
#holaconnombre(name = str(input("Ingrese un nombre: ")))

#------------------------------------------------------

def multplica(val1,val2):     #la función recibe valores
   print( val1*val2)
#multplica(3,5)

#------------------------------------------------------
def gravity():                                  
    x = 9.81
    print(x , id (x) , sep =" ------> ")
def pi():
    x = 3.1416
    print(x , id (x) , sep =" ------> ")
#pi()
#gravity()
#print()

#------------------------------------------------------
n = 6.02
def gravity():
    x = 9.81
    print('Local')
    print(x , id (x) , sep =" ------> ")
    print('Global')
    print(n , id (n) , sep =" ------> ")
def pi():
    x = 3.1416
    print('Local')
    print(x , id (x) , sep =" ------> ")
    print('Global')
    print(n , id (n) , sep =" ------> ")

#gravity()
#pi()
#print('Main - Global')
#print(n, id(n), sep='----->')

#------------------------------------------------------
def countdown(n):
    print(n)
    if n>0:
        print(n-1)
#countdown(6)

#------------------------------------------------------

#histograma

def procedimiento(num):
    i = 0
    for i in range(0,num):
        print('*')  

def mainnum():  
    num = 1
    while num!= 0: 
        num = int(input("Ingrese un número: "))
        #procedimiento(num)    
#mainnum()

#------------------------------------------------------

#sumaymultiplicacion

def lista():
    listanum=[]
    rpta = int(input("¿Cuántos elementos tendrá la lista?" ))
    i = 0
    for i in range(0,rpta):
        b = int(input("Ingrese el elemento: "))
        listanum.append(b)
    print("La lista armada por el usuario es: ",listanum)
    sum(listanum)
    mult(listanum)

def sum(listanum):
    
    rpta = len(listanum)
    i=0
    b=0
    for i in range(0,rpta):
        b=listanum[i]+b
    print("La suma de los elementos de la lista: ",b)

def mult(listanum):
    
    rpta =len(listanum)
    i=0
    b=1
    for i in range(0,rpta):
        b=listanum[i]*b
    print("La multiplicación de los elementos : ",b)
#lista()

#------------------------------------------------------

def promedio(x,y,z):
    return (x+y+z)/3

def prom():
    n1 = int(input("Ingrese primer numero: "))
    n2 = int(input("Ingrese segundo numero: "))
    n3 = int(input("Ingrese tercer numero: "))
    print("El promedio de los tres es: ", promedio(n1,n2,n3))
#prom()

#------------------------------------------------------

def mayordedos(x,y): 
    if x>y: 
        return x
    else: 
        return y

def mayordetres(x,y,z):
    if mayordedos(x,y)==x: 
        if mayordedos(x,y)==x:
            return x
        else: 
            return z
    else : 
        if mayordedos(y,z) == y:
            return y
        else: 
            return z

def mayores():
    n1 = int(input("Ingrese primer numero: "))
    n2 = int(input("Ingrese segundo numero: "))
    n3 = int(input("Ingrese tercer numero: "))
    print("El número mayor es: ", mayordetres(n1,n2,n3))
#mayores()       