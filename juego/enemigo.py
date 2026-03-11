import os
import random
import numpy as np
from .barco import TIPOS_BARCOS

def iniciar_bot(tablero_iniciado):
    for n in TIPOS_BARCOS:
        barco = TIPOS_BARCOS[n][0]
        contador = TIPOS_BARCOS[n][1]
        
        while contador > 0:
            orientacion = random.randint(0, 1)
            
            if orientacion == 0:
                altitud = random.randint(0, 9 - barco.tamanno)
                longitud = random.randint(0, 9)
                zona = tablero_iniciado[0, altitud:altitud + barco.tamanno, longitud]
            else:
                altitud = random.randint(0, 9)
                longitud = random.randint(0, 9 - barco.tamanno)
                zona = tablero_iniciado[0, altitud, longitud:longitud + barco.tamanno]
            
            if np.all(zona == "_"):
                contador -= 1
                barco.fletar(orientacion, altitud, longitud, tablero_iniciado, 0)
            
def disparar_bot(tablero_iniciado):
    from .partida import apuntar, victoria, mostrar_tablero

    i = random.randint(0, 9)
    j = random.randint(0, 9)


    if tablero_iniciado[2, i, j] in ("b", "d"):
        print("¡Te han dado!")
        tablero_iniciado[2, i, j] = "x"
        input("")
        disparar_bot(tablero_iniciado)
        victoria(tablero_iniciado)
    else:
        print("¡El enemigo ha fallado!")
        tablero_iniciado[2, i, j] = "O"
        input("")
        apuntar(tablero_iniciado)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TU TABLERO ===")
    mostrar_tablero(tablero_iniciado[2])
    print("=== TABLERO DE DISPAROS ===")
    mostrar_tablero(tablero_iniciado[1])
    