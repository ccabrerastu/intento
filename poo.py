class fraccion: 
    def partes(self,numerador,denominador):
        self.numerador=numerador 
        self.denominador=denominador  
    
    def fracc(self):    
        print(self.numerador, "/",self.denominador)
    
    
fr=fraccion()   
fr2=fraccion()

fr.partes(25,10)
fr2.partes(3,13)

fr.fracc()
fr2.fracc()

#clase->fraccion
#atributos-> numerador y denominador
