#LIBRERIAS
# ==========================================================================================================================================================
from tkinter import *
import os
import time
from io import open

# VARIABLES GLOBALES
# ==========================================================================================================================================================
lista=list()
num_pacientes=0

# REGISTRO
# ==========================================================================================================================================================
class paciente:
    def __init__(self):
        self.nombre={""}
        self.edad={""}
        self.sexo={""}
        self.nacionalidad={""}
        self.dni={""}
        self.padecimiento={""}
        self.sangre={""}
        self.donador={""}
        self.estado={""}

# Este comando sirve para limpiar la consola
os.system("cls")
print("------ SELECCIONE UNA OPCION DE LA INTERFAZ ------")

# FUNCIONES
# ==========================================================================================================================================================
def registrar():
    os.system("cls")

    # El global sirve para utilizar variables que estan fuera de la función
    global num_pacientes

    # Aqui se declara la clase paciente en una variable para poder acceder a sus atributos
    persona=paciente()

    print("================================")
    print("         NUEVO PACIENTE         ")
    print("================================")
    print("")

    persona.nombre=input("Nombre completo: ")
    # El upper es para convertir todo el texto en MAYÚSCULA
    persona.nombre=persona.nombre.upper()

    persona.edad=int(input("Edad: "))
    persona.sexo=input("Sexo: ")
    persona.sexo=persona.sexo.upper()

    persona.nacionalidad=input("País: ")
    persona.nacionalidad=persona.nacionalidad.upper()

    persona.dni=input("DNI: ")
    persona.padecimiento=input("Padecimiento: ")
    persona.padecimiento=persona.padecimiento.upper()

    persona.sangre=input("Tipo de sangre: ")
    persona.sangre=persona.sangre.upper()

    persona.donador=input("Donante: ")
    persona.donador=persona.donador.upper()
    print("")

    if persona.edad<14 or persona.sexo=="FEMENINO":
        persona.estado="PREFERENCIAL"
    else:
        persona.estado="NO PREFERENCIAL"

    lista.append(persona)
    num_pacientes=num_pacientes+1
    
    print("Registrando...")

    # Este comando sirve para pausar por unos segundos el programa
    time.sleep(2)

    os.system("cls")
    print("El paciente ha sido registrado en el sistema.")
    print("")
    exit=input("Presione enter para continuar.")
    os.system("cls")

    print("------ SELECCIONE UNA OPCION DE LA INTERFAZ ------")
    

def mostrar():
    os.system("cls")

    for persona in lista:
        print("Nombre:",persona.nombre)
        print("DNI:",persona.dni)
        print("Estado:",persona.estado)
        print("--------------------------------")

    print("")
    print("PACIENTES REGISTRADOS:",num_pacientes)
    print("")
    exit=input("Presione enter para continuar.")
    os.system("cls")

    print("------ SELECCIONE UNA OPCION DE LA INTERFAZ ------")


def actualizar():
    os.system("cls")

    print("================================")
    print("       ACTUALIZAR REGISTRO      ")
    print("================================")
    print("")

    dni=input("DNI del paciente: ")
    print("")

    for persona in lista:

        if persona.dni==dni:
            print("Nombre:",persona.nombre)
            print("")
            edit=(input("¿Desea editar el registro?: "))
            edit=edit.upper()
            print("")

            if edit=="SI":
                os.system("cls")

                print("--------------------------------")
                print("       ACTUALIZANDO DATOS       ")
                print("--------------------------------")
                print("")

                persona.nombre=input("Nombre completo: ")
                persona.nombre=persona.nombre.upper()

                persona.edad=int(input("Edad: "))
                persona.sexo=input("Sexo: ")
                persona.sexo=persona.sexo.upper()

                persona.nacionalidad=input("País: ")
                persona.nacionalidad=persona.nacionalidad.upper()

                persona.dni=(input("DNI: "))
                persona.padecimiento=input("Padecimiento: ")
                persona.padecimiento=persona.padecimiento.upper()

                persona.sangre=input("Tipo de sangre: ")
                persona.sangre=persona.sangre.upper()

                persona.donador=input("Donante: ")
                persona.donador=persona.donador.upper()
                print("")

                if persona.edad<14:
                    persona.estado="PREFERENCIAL"
                else:
                    persona.estado="NO PREFERENCIAL"
    
                if persona.sexo=="FEMENINO":
                    persona.estado="PREFERENCIAL"
                else:
                    persona.estado="NO PREFERENCIAL"

                print("Actualizando datos...")
                time.sleep(2)
                os.system("cls")
                print("Datos actualizados correctamente.")
                print("")
                exit=input("Presione enter para continuar.")
                os.system("cls")

            else:
                edit=="NO"  
                exit=input("Presione enter para continuar.")
                os.system("cls") 

    print("------ SELECCIONE UNA OPCION DE LA INTERFAZ ------")


def buscar_dni():
    os.system("cls")

    print("================================")
    print("      BUSQUEDA DE PACIENTE      ")
    print("================================")
    print("")

    dni=input("DNI del paciente: ")
    print("")

    for persona in lista:
        if persona.dni==dni:
            os.system("cls")
            print("--------------------------------")
            print("       DATOS DEL PACIENTE       ")
            print("--------------------------------")
            print("")
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

    exit=input("Presione enter para continuar.")
    os.system("cls")

    print("------ SELECCIONE UNA OPCION DE LA INTERFAZ ------")


def buscar_donantes():
    os.system("cls")

    print("================================")
    print("       PACIENTES DONADORES      ")
    print("================================")
    print("")

    for persona in lista:
        if persona.donador=="SI":
            print("Edad:",persona.edad)
            print("DNI:",persona.dni)
            print("")

    exit=input("Presione enter para continuar.")
    os.system("cls")

    print("------ SELECCIONE UNA OPCION DE LA INTERFAZ ------")

def descargar():

    os.system("cls")
    print("Descargando datos...")
    time.sleep(3)
    os.system("cls")

    # Se declara una nueva variable que convierte a otra variable tipo int en string
    num_text=str(num_pacientes)

    # Se crea un archivo de texto con los pacientes registrados, solo muestra nombre y dni pero se pueden agregar todos los datos
    archivo=open("REGISTRO DE PACIENTES.txt","w")
    archivo.write("PACIENTES REGISTRADOS: ")
    archivo.write(num_text)
    archivo.write("\n")
    archivo.write("-------------------------\n")
    archivo.write("\n")
    for persona in lista:
        archivo.write("Nombre: ")
        archivo.write(persona.nombre)
        archivo.write("\n")
        archivo.write("DNI: ")
        archivo.write(persona.dni)
        archivo.write("\n")
        archivo.write("\n")
    archivo.close()

    print("Datos descargados con exito.")
    print("")
    exit=input("Presione enter para continuar.")
    os.system("cls")

    print("------ SELECCIONE UNA OPCION DE LA INTERFAZ ------")

# INTERFAZ GRÁFICA
# ==========================================================================================================================================================

# Creación de la ventana principal
mywindow=Tk()
mywindow.geometry("650x550")
mywindow.title("Programa ODS Salud y Bienestar")
mywindow.resizable(False, False)
mywindow.config(background="#23272A")
main_title=Label(text="HOSPITAL COMUNITARIO | Salud y Bienestar", font=("Fira sans", 16), bg="#5865F2", fg="white", width="500", height="2")
main_title.pack()

mostrar_boton=Button(mywindow,text="Visualizar registro de pacientes", font=("Fira sans", 10), width="30", height="2", command=mostrar, bg="#FEE75C")
mostrar_boton.place(x=215, y=185)

actualizar_boton=Button(mywindow,text="Actualizar ficha de paciente", font=("Fira sans", 10), width="30", height="2", command=actualizar, bg="#FEE75C")
actualizar_boton.place(x=215, y=245)

buscarDNI_boton=Button(mywindow,text="Buscar paciente", font=("Fira sans", 10), width="30", height="2", command=buscar_dni, bg="#FEE75C")
buscarDNI_boton.place(x=215, y=305)

buscarDonante_boton=Button(mywindow,text="Lista de donantes", font=("Fira sans", 10), width="30", height="2", command=buscar_donantes, bg="#FEE75C")
buscarDonante_boton.place(x=215, y=365)

informe_boton=Button(mywindow,text="DESCARGAR INFORME", font=("Fira sans", 12), width="30", height="2", command=descargar, bg="#ED4245")
informe_boton.place(x=185, y=455)

mywindow.mainloop()
