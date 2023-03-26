# def saludo(nombre):
#    print('¡Hola' , nombre , '!!!!!')   
# saludo("Camila")
# saludo("Fernanda")


#def area_circulo(radio):
#    pi = 3.1415
#    area = pi*radio**2
#    print("El area es: ",  area)
# area_circulo(radio=int(input("Ingrese el radio:   ")))


#def volumen_cilindro(radio,altura):
#    volumen = (3.14* radio**2) * altura
#    return(volumen)
#radio=int(input("Ingrese el radio: "))
#alt=int(input("Ingrese altura: "))
#print("El volumen es: ", volumen_cilindro(radio,alt))


# def cuadrados(list):    
#    for i in range(0,len(list)):
#        list.append(list[i]*list[i])
#    return(list)
# print("La nueva tupla con sus cuadrados es: ", cuadrados([1,2,3,4,5]))
# print("La nueva tupla con sus cuadrados es: ", cuadrados([2.3,5.7,6.8,9.7,12.1,15.6]))


# def nexo(a,b):
#    if a > b :
#        return 1
#    elif a < b : 
#        return -1 
#    else : 
#        return 0
#a = float(input("Ingrese el primer valor: "))
#b = float(input("Ingrese un segundo valor: "))
#print("""
# - SI EL PRIMER Nº ES MAYOR QUE EL SEGUNDO -> 1
# - SI EL PRIMER Nº ES MENOR QUE EL SEGUNDO -> -1
# - SI AMBOS NUMEROS SON IGUALES -> 0
#""")
#print (nexo(a,b))
#print (nexo(10,5))
#print (nexo(5,5))


#def recorte(num,min,max):
#    if num < min:
#        return(min)
#    elif num > max : 
#        return (max)
#    else: 
#        return num 
#num = int(input("Ingrese un numero: "))
#min = int(input("Ingrese un numero minimo: "))
#max = int(input("Ingrese un numero maximo: "))
#print("El resultado es: ", recorte(num,min,max))
#print("El resultado es: ",recorte(15,0,10))



#def rutina():
#    def sub_rutina():
#        print(a)
#        return

#    a = int(input("Ingrese un valor: "))
#    sub_rutina()
#    print(a)
#    return
#a = 4
#rutina()
#print(a)


#def operador(n): 
#    tmp = 1
#    for i in range (n): 
#        tmp *= i + 1
#        print(tmp)
#print(operador(20))


#def mcd (n,m):
#    r = 0
#    while(m > 0):
#        rest = m
#        m = n % m
#        n = rest
#    return(n)

#def mcm(n,m):
#    if n > m : 
#        greater = n 
#    else : 
#        greater = m
#    while (greater % n!=0) or (greater %m != 0 ): 
#        greater += 1
#    return (greater)
#num=int(input("Ingrese un valor: "))
#max=int(input("Ingrese un valor máximo: "))
#print("El máximo común divisor es: " , mcd(num,max))
#print("El minímo común máximo es: " ,mcm(num,max))