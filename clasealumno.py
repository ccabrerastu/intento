
class alumno:   #<-----CLASE
    def datosatributos(self,nombre,nota):
        self.nombre=nombre  #<-----Atributos
        self.nota=nota      #<-----Atributos
    
    #Metodos para usar los atributos
    def imprimir(self):     #<-----Funcion que imprimira los nombres y calificaciones.
        print("-------------------")
        print("Nombre: ",self.nombre)
        print("Calificacion: ",self.nota)
    
    def resultado(self):    #<-----Funcion para determinar si el alumno esta aprobado o no, de acuerdo a la condicion
        if self.nota<11:
            print("Alumno reprobado")
            
        else:
            print("Alumno aprobado")
            
    
alumno1=alumno()   
alumno2=alumno()

#<-----Datos enviados a los atributos ("nombre", nota)
alumno1.datosatributos("Gerald ",12)
alumno2.datosatributos("Junco ",10)

#<-----Mostrara en pantalla la funcion imprimir, para los dos alumnos.
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()