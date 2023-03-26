def ejer1():
    import array as arr
    a=arr.array('b',[1,2,3,4,5])
    i=0
    while i<5:
        a[i]=int(input("Ingrese uno de los valores"))
        i=i+1
    print(a)
#ejer1()

def ejer2():
    import array as arr
    a=arr.array('b',[])
    i=0
    j=int(input("Ingrese el tamaño del array: "))
    while i<j:
        b=int(input("Ingrese uno de los valores"))
        a.append(b)
        i=i+1
    print(a)
#ejer2()
def ejer3():
    import array as arr
    a=arr.array('f',[])
    b=arr.array('f',[])
    c=arr.array('f')
    y=0
    
    i=0
    r=int(input("Ingrese el tamaño del array: "))
    while i<r:
        q=float(input("Ingrese uno de los valores"))
        a.append(q)
        i=i+1
    j=int(input("Ingrese el tamaño del array: "))
    while i<j:
        q=float(input("Ingrese uno de los valores"))
        b.append(q)
        i=i+1
    c=a+b

    print(c[0:r+1])
    print(c[r:j+r-1])
#ejer3()

def ejer4():
    import array as arr
    a=arr.array('b',[])
    b=arr.array('b',[])
    r=int(input("Ingrese el tamaño del array: "))
    i=0
    while i<r:
        q=int(input("Ingrese uno de los valores"))
        a.append(q)
        i=i+1
    j=int(input("Ingrese el tamaño del array: "))
    i=0
    while i<j:
        q=int(input("Ingrese uno de los valores"))
        b.append(q)
        i=i+1
    i=0
    suma=0
    for i in range(r):
        suma=suma+a[i]
    resta=b[0]-b[1]
    print(resta)
    i=2
    while i<j:
        resta=resta-b[i]
        i=i+1

    print(suma)
    print(resta)

    
ejer4()