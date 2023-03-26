
def saludo(nombre):
    print('¡Hola',nombre,'!')
#saludo("Liliana")
#saludo("Mercedes")

def areacirculo(radio):
    pi=3.1415
    area=pi*(radio**2)
    return(area)
# radio=int(input("Ingrese el radio del circulo"))
# print(areacirculo(3))


def volumen_cilindro(radio,altura):
    pi=3.1415
    volumen=pi*(radio**2)*altura
    return(volumen)
# radio=int(input("ingrese el radio "))
# altura=int(input("ingrese la altura "))
# print(volumen_cilindro(radio,altura))

#  [ ]

def cuadrados(list):    
    for i in range(0,len(list)):
        list.append(list[i]*list[i])
    return(list)
# print(cuadrados([1,2,3,4,5]))
# print(cuadrados([2.3,5.7,6.8,9.7,12.1,15.6]))

def anexados(a,b):
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0
# a=int(input("ingrese el primer valor: "))
# b=int(input("ingrese el segundo valor: "))
# print(anexados(a,b))
# print(anexados(5,10))
# print(anexados(10,5))
# print(anexados(5,5))

def recortar(a,b,c):
    if a<b:
        return b
    elif a>c:
        return c
    else:
        return a
#print(recortar(15,0,10))

def subrutina():
    def sub_subrutina():
        print(a)
        return
    a=3
    sub_subrutina()
    print(a)
    return
a=4
subrutina()
print(a)

def operador(n):
    tmp=1
    for i in range(n):
        tmp*=i+1
        print(tmp) 
# print(operador(20))

def mcd(n,m):
    rest=0
    while m>0:
        rest=m
        m=n%m
        n=rest
    return n
def mcm(n,m):
    if n>m:
        greater=n
    else:
        greater=m
    while (greater%n!=0) or (greater% m!=0):
        greater+=1
    return greater
# a=int(input("Ingrese un numero: "))
# b=int(input("Ingrese un numero: "))
# print(mcd(a,b))
# print(mcm(a,b))

