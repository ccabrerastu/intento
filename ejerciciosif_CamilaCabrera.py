from lib2to3.pgen2.tokenize import TokenError


def alquiler_vehiculo():
    recorrido = float (input("Ingrese el recorrido del vehiculo: "))
    if recorrido <= 300 : 
        print ("Usted debe pagar la cantidad de S/. 300 soles")
    elif recorrido > 300 and recorrido <=1000 : 
        adicional = 50 * (recorrido  - 300)
    else : 
        adicional = 100 * (recorrido  - 1000)
    print("El cobro por cada 100 km recorrido es: ", (300 + adicional)/100 )
    print("El cobro por alquiler de vehiculo es: ", 300 + adicional )

def ejercicio2():
    juan = int (input("Ingrese la edad de Juan: "))
    mario = int (input("Ingrese la edad de Mario: "))
    pedro = int (input("Ingrese la edad de Pedro: "))
    dif1 = juan - mario 
    dif2 = juan - pedro
    dif3 = mario - pedro
    if dif1 <= dif2 and dif1 <= dif3 : 
        print ("Juan y Mario son contemporaneos")
    elif dif2 <= dif1 and dif2 <= dif3: 
        print ("Juan y Pedro son contemporaneos")
    elif dif3 <= dif1 and dif3 <= dif2: 
        print (" Mario y Pedro son contemporaneos")
    else : 
        print ("Los tres con contemporaneos")

def ejercicio3(): 
    gasto = float(input("Ingrese la cantidad a pagar: "))
    if gasto < 100 : 
        print ("Pague con dinero en efectivo")
    elif gasto>=100 or gasto<300 : 
        print ("Pague con tarjeta de debito")
    else: 
        print ("Debe pagar con trajeta de credito")

    if gasto>100 : 
        print ("Obtuvo un descuento de " ,(gasto * 0.10), "soles")

def ejercicio4(): 
    n1 = int (input("Ingrese el primer numero: "))
    n2 = int (input("Ingrese el segundo numero: "))
    n3 = int (input("Ingrese el tercer numero: "))
    if n1 < n2 and n1 < n3 : 
       print ("El menor numero es " , n1)
    elif n2 < n1 and n2 < n3 : 
       print ("El menor numero es " , n2)  
    elif n3 < n1 and n3 < n2 : 
       print ("El menor numero es " , n3) 
    else: 
        print ("Los tres numeros son iguales")

def ejercicio5(): 
    ninas = int (input ("Ingrese el numero de ninas: "))
    ninos = int (input ("Ingrese el numero de ninos: "))
    total = ninas + ninos
    pninas = (ninas * 100 ) / total
    pninos = 100 - pninas
    print("Hay un " , pninas ," % de ninas y un " , pninos ," % de ninos" )
    if pninas > pninos :
        print ("El mayor porcentaje es de la ninas")
    elif pninos > pninas : 
        print ("El mayor porcentaje es de la ninos")
    else : 
        print ("Ninos y ninas tienen el mismo porcentaje")

def ejercicio6(): 
    practica = float (input ("Ingrese la nota de practicas: "))
    problemas = float (input ("Ingrese la nota de la parte problemas: "))
    teorica = float (input ("Ingrese la nota de teoria: "))
    total = (practica * 0.10 ) + (problemas * 0.50) + (teorica * 0.40)
    if 0 <=total and total<= 10 :
        print("Su nota es " , total, "esta desaprobado")
    elif 11 <=total and total<= 16 : 
        print("Su nota es " , total, "esta aprobado")
    else : 
        print("Su nota es " , total, "esta destacado")

