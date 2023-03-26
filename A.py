#OPCIONES IMPLEMENTADAS:

#1. Registrar paciente
#2. Ver registro de pacientes
#3. ----
#4. Buscar paciente por DNI
#5. Lista de pacientes donadores

lista=list()

class paciente:
    def __init__(self):
        self.nombre={""}
        self.edad={}
        self.sexo={""}
        self.nacionalidad={""}
        self.dni={}
        self.padecimiento={""}
        self.sangre={""}
        self.donador={""}
        self.estado={""}

num_pacientes=0

def registrar():
    persona=paciente()

    persona.nombre=input("Nombre completo: ")
    persona.nombre=persona.nombre.upper()

    persona.edad=int(input("Edad: "))
    persona.sexo=input("Sexo: ")
    persona.sexo=persona.sexo.upper()

    persona.nacionalidad=input("País: ")
    persona.nacionalidad=persona.nacionalidad.upper()

    persona.dni=int(input("DNI: "))
    persona.padecimiento=input("Padecimiento: ")
    persona.padecimiento=persona.padecimiento.upper()

    persona.sangre=input("Tipo de sangre: ")
    persona.sangre=persona.sangre.upper()

    persona.donador=input("Donante: ")
    persona.donador=persona.donador.upper()

    if persona.edad<14:
        persona.estado="PREFERENCIAL"
    else:
        persona.estado="NO PREFERENCIAL"
    
    if persona.sexo=="FEMENINO":
        persona.estado="PREFERENCIAL"
    else:
        persona.estado="NO PREFERENCIAL"

    lista.append(persona)


def mostrar():
    print("PACIENTES REGISTRADOS:",num_pacientes)
    print("")

    for persona in lista:
        print("PACIENTE",12)
        print("Nombre:",persona.nombre)
        print("DNI:",persona.dni)
        print("Estado:",persona.estado)
        print("")

def buscar4():
    dni=int(input("DNI: "))
    print("")

    for persona in lista:
        if persona.dni==dni:
            print("Nombre:",persona.nombre)
            print("Edad:",persona.edad)
            print("Sexo:",persona.sexo)
            print("País",persona.nacionalidad)
            print("DNI:",persona.dni)
            print("Padecimiento:",persona.padecimiento)
            print("Tipo de sangre:",persona.sangre)
            print("Donante:",persona.donador)
            print("Estado:",persona.estado)
            print("")

def buscar5():

    for persona in lista:
        if persona.donador=="SI":
            print("Edad:",persona.edad)
            print("DNI:",persona.dni)
            print("")


#Este menú tiene que ser convertido en una interfaz gráfica.
op=1
while op==1:
    main=int(input("""
    Ingrese una opción 
    1.Agregar
    2.Muestras 
    4.Buscar por DNI 
    5.Lista de donadores: 
    """))
    print("")

    if main==1:
        registrar()
        num_pacientes=num_pacientes+1
    elif main==2:
        mostrar()
    elif main==4:
        buscar4()
    elif main==5:
        buscar5()

    op=int(input("ingrese 1 para volver o 0 para cerrar: "))
    print("")
