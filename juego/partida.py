"""Módulo para la lógica de disparos."""
import os
from .enemigo import disparar_bot

def disparo(i, j, tablero_iniciado):
    '''
    Recive las coordenadas de la función entrada() para comprobar si en el sitio
    había o no un barco y volver a efectuar otro disparo o no.
    '''

    if tablero_iniciado[0, i-1, j-1] in ("b", "d"):
        print("¡Tocado!")
        tablero_iniciado[1, i-1, j-1] = "x"
        input("")
        apuntar(tablero_iniciado)
    else:
        print("¡Agua!")
        tablero_iniciado[1, i -1, j -1] = "O"
        input("")
        disparar_bot(tablero_iniciado)
        
    os.system('cls' if os.name == 'nt' else 'clear')
    print(tablero_iniciado[1:])


def apuntar(tablero_iniciado):
    '''
    Entrada del juego, con validación rudimentaria de la entrada del usuario.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print(tablero_iniciado[1:])
    
    i = int(input("Apunta a la fila: "))
    j = int(input("Y a la columna: "))

    while True:
        if i < 1 or i > 10 or j < 1 or j > 10:
            print("Fuera de rango!")
            i = int(input("fila: "))
            j = int(input("columna: "))
        else:
            disparo(i, j, tablero_iniciado)
            break