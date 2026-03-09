import numpy as np



tablero = np.full(((10, 10)), "_", dtype=str)
# galeon =
bergantin = np.array(["b", "b", "b", "b"])
carabela = np.array(["b", "b", "b"])

tablero[1, 0:4] = bergantin
tablero[3:6, 3] = carabela
print(tablero)



def entrada():
    '''
    Entrada del juego, con validación rudimentaria de la entrada del usuario.
    '''
    i = int(input("i: "))
    j = int(input("j: "))
    
    while True:
        if i < 1 or i > 10 or j < 1 or j > 10:
            print("¡Fuera de rango!")
            i = int(input("i: "))
            j = int(input("j: "))
        else:
            disparo(i, j)
            break


def disparo(i, j):
    '''
    Recive las coordenadas de la función entrada() para comprobar si en el sitio
    había o no un barco y volver a efectuar otro disparo o no.
    '''
    if tablero[i -1, j -1] == "b":
        print("¡Tocado!")
        tablero[i -1, j -1] = "x"
        entrada()
        return True
    else:
        print("¡Agua!")
        tablero[i -1, j -1] = "O"
        return False
print(tablero)
    
entrada()