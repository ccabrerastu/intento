class Persona:                                              # Se crea la superclase Persona
    def __init__(self,nombre,edad):                         
        self.nombre=nombre                                  # Atributos
        self.edad=edad                                      # Atributos
class Maestro(Persona):                                     # Se crea la subclase Maestro que hereda a la superclase Persona
    def __init__(self,nombre,edad,grado):
        Persona.__init__(self,nombre,edad)
        self.grado=grado                                    # Atributos
class Estudiante(Persona):                                  # Se crea la subclase Estudiante que herada la superclase Persona
    def __init__(self,nombre,edad,codigo):
        Persona.__init__(self,nombre,edad)
        self.codigo=codigo                                  # Atributos
class Universitario(Estudiante):                            # Se crea la subclase Universitario que herada la subclase estudiante
    def __init__(self,nombre,edad,codigo,carrera):
        Estudiante.__init__(self,nombre,edad,codigo)
        self.carrera=carrera                                # Atributos

u1=Universitario("Carlos",19,"2021070016","Sistemas")       # Se crea la instancia u1 y se le agregan sus datos correspondientes
m1=Maestro("Juan",19,"Ingeniero")                           # Se crea la instancia m1 y se le agregan sus datos correspondientes

print(u1.carrera)                                           # Se llama a la instancia u1 para que muestre el dato indicado que vendría a ser carrera

print(m1.nombre)                                            # Se llama a la instancia m1 para que muestre el dato indicado que vendría a ser su nombre