
from battleship.Orientacion import Orientacion
from battleship import Impacto

class Tablero():
    
    def __init__(self, tamano: int):
        self._tablero = [(["O"] * tamano) for _ in range(tamano)]
        
    def imprimir(self):
        print("Batalla naval")
        print("--------------")
        for i in self._tablero:
            print(" ".join(i))
            
   
    def ubicar_barco(self, barco: Barco, x: int, y: int):
        for i in range(barco.tamano):
            if barco.orientacion == Orientacion.HORIZONTAL:
                self._tablero[x + i][y] = barco
            elif barco.orientacion == Orientacion.VERTICAL:
                self._tablero[x][y + i]
                
                
    def impacto_barco(self, barco: Barco):
        for i in range(barco.tamano):
            if barco.impacto == Impacto.POSITIVO:
                barco.tamano = barco.tamano -1
            elif barco.impacto == Impacto.NEGATIVO:
                barco.tamano = barco.tamano -0
                
        return barco.tamano
    
    def hundir_barco(self, barco: Barco) -> bool:
        for i in range(barco.tamano):
            if barco.tamano == Impacto.POSITIVO and barco.tamano == 1:
                return True
        return False
                
                
                 
                