from random import randint  
from battleship import Orientacion, Tablero

class barco():
    def __init__(self, orientacion, tamano ):
        self.orientacion = orientacion
        self.tamano = tamano
    
    def orientacion_barco(self, orientacion: int) -> bool:    
        if orientacion == Orientacion.HORIZONTAL or Orientacion.VERTICAL:
            self.orientacion = orientacion
            return True
        return False
    
    
    def impacto_barco(self):
        for i in range(self._tablero):
            if Tablero.Ubicar_barco == "*":
                return True
            elif Tablero.Ubicar_barco == "0":
                return False
            
            
    def hundir_barco(self, tamano):
        for i in range(self._tablero):
            if tamano == Tablero.Ubicar_barco:
                return True
            return False
