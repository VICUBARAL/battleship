from random import randint  

class barco():
    def __init__(self, orientacion, tamano ):
        self.tamano = tamano
    
    def orientacion_barco(self, orientacion):    
        if orientacion == "horizontal" or orientacion == "vertical":
            self.orientacion = orientacion
        else:
            print("La posición del barco debe ser horizontal o vertical")
            
    def ubicacion_barcos(self, tamano, orientacion):
        if orientacion == "horizontal":
            if tamano <= #Tablero.tamano:
                #Tablero.append(barco())               
        

