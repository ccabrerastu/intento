lista=list()
num_pacientes=0

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


def actualizar():
    dni=int(input("DNI del paciente: "))
    print("")

    for persona in lista:

        if persona.dni==dni:
            print("Nombre:",persona.nombre)
            edit=(input("¿Desea editar el registro?: "))
            edit=edit.upper()

            if edit=="SI":

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
        else:
            print("Paciente no registrado.")


def buscar_dni():
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


def buscar_donantes():

    for persona in lista:
        if persona.donador=="SI":
            print("Edad:",persona.edad)
            print("DNI:",persona.dni)
            print("")

#Este menú tiene que ser convertido en una interfaz gráfica.

op_doc=1
while op_doc==1:

    doc=int(input("ingrese una opción 1.agrega 2.mostrar 3.editar 4.buscar dni 5.lista donadores:"))
    print("")

    if doc==1:
        registrar()
        num_pacientes=num_pacientes+1
        op_doc=int(input("ingrese 1 para volver al menú o 0 para cerrar: "))
        print("")

    elif doc==2:
        mostrar()
        op_doc=int(input("ingrese 1 para volver al menú o 0 para cerrar: "))
        print("")

    elif doc==3:
        actualizar()
        op_doc=int(input("ingrese 1 para volver al menú o 0 para cerrar: "))
        print("")

    elif doc==4:
        buscar_dni()
        op_doc=int(input("ingrese 1 para volver al menú o 0 para cerrar: "))
        print("")

    elif doc==5:
        buscar_donantes()
        op_doc=int(input("ingrese 1 para volver al menú o 0 para cerrar: "))
        print("")

    elif doc==0:
        op_doc=0

    else:
        print("Opción invalida.")
        print("")
        op_doc=int(input("ingrese 1 para volver al menú o 0 para cerrar: "))
        print("")