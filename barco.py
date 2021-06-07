from random import randint  
from battleship import Orientacion, Tablero

class barco():
    def __init__(self, orientacion, tamano, impacto):
        self.orientacion = orientacion
        self.tamano = tamano
        self.impacto = impacto
        
    
    def orientacion_barco(self, orientacion: int) -> bool:    
        if orientacion == Orientacion.HORIZONTAL or Orientacion.VERTICAL:
            self.orientacion = orientacion
            return True
        return False
    
    
   
