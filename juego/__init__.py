"""Paquete del juego Batalla Naval."""

import os
import numpy as np
from .configuracion import entrada
from .partida import apuntar, disparo, mostrar_tablero
from .barco import Barco, TIPOS_BARCOS
from .enemigo import iniciar_bot

def iniciar():
    # z = int(input("Introduce el tamanno del tablero: "))
    tablero = np.full((3, 10, 10), "_", dtype=str)


    iniciar_bot(tablero)

    os.system('cls' if os.name == 'nt' else 'clear')
    mostrar_tablero(tablero[0])
    input("enter: ")

    entrada(tablero)

    apuntar(tablero)

__all__ = ["iniciar", "entrada", "apuntar", "disparo", "crear_tablero", "mostrar_tablero", "Barco", "TIPOS_BARCOS"]