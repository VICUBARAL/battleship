
tablero = []
barco_uno = 3
barco_dos = 3
barco_tres = 3

def crear_tablero():
    for x in range(9):
        tablero.append(["O"] * 9)
        
def imprimir_tablero():
    print("Batalla naval")
    print("--------------")
    for i in tablero:
        print(" ".join(i))
        
        

