class Tablero():
    
    tablero = []
    
    def __init__(self, tamano: int):
        self._tablero = [(["O"] * tamano) for _ in range(tamano)]
        
    def imprimir(self):
        print("Batalla naval")
        print("--------------")
        for i in self._tablero:
            print(" ".join(i))