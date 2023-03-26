def ejercicio2():
    a = 0
    emayor = 0
    emenor = 0
    estudiantes = int(input("Ingrese el numero de estudiantes: "))
    suma = 0
    while a < estudiantes :
        edad = int(input("Ingrese la edad del estudiante: "))
            suma = suma + edad
            a = a + 1
            prom = float(suma / estudiantes)
    print ("El promedio de las edades son: ", prom)

ejercicio2()
