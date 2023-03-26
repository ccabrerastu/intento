print ("""
BIENVENIDO AL SISTEMA DE REGISTROS 
¿ Ud ingresa como ?
1. Médico
2. Paciente
""")
op = int(input("Ingrese una opción: "))

i = 0
def medico(): 
    i = 0
    if op == 1 : 
        while i<3: 
            usuario = str(input("Ingrese usuario: "))
            i = i + 1
            if str(usuario)=="medico04": 
                contra = str(input("Ingrese contraseña: "))
                if str(contra)=="medicoayuda":
                    print("Bienvenido Doctor@")
                else:
                    print("Clave incorrecta")
                    if i ==3: 
                        print ("Muchos intentos")
            else: 
                print("Usuario incorrecto")
                if i==3: 
                    print ("Muchos intentos")
#medico()           

def paciente():
    if op == 2: 
        dni = int(input("Ingrese su DNI: "))
        for datos_pacientes in range : 
            print ()
