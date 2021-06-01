
from battleship.Orientacion import Orientacion

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