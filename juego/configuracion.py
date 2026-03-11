"""Módulo para configuración inicial."""

import os
import numpy as np
from .barco import TIPOS_BARCOS

def mostrar_dique():
    print("Barcos en el dique")
    for clave, (barco, cantidad) in TIPOS_BARCOS.items():
        if cantidad > 0:
            print(f"{clave}: {barco.nombre} tamano: {barco.tamanno} - cantidad: {cantidad}")


def obtener_coordenadas():
    orientacion = int(input("Vertical(0) / Horizontal(1): "))
    altitud = int(input("Altitud del barco: ")) - 1
    longitud = int(input("Longitud del barco: ")) - 1
    return orientacion, altitud, longitud


def validar_colocacion(barco, orientacion, altitud, longitud, tamanno_tablero, tablero_iniciado):
    if orientacion == 0:       
        if altitud + barco.tamanno > tamanno_tablero:
            return False
        zona = tablero_iniciado[2, altitud:altitud + barco.tamanno, longitud]
    else:
        if longitud + barco.tamanno > tamanno_tablero:
            return False
        zona = tablero_iniciado[2, altitud, longitud:longitud + barco.tamanno]
    return np.all(zona == "_")



def entrada(tablero_iniciado):
    tamanno_tablero = tablero_iniciado.shape[1]
    while any(cantidad > 0 for _, (_, cantidad) in TIPOS_BARCOS.items()):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(tablero_iniciado[2])
        
        mostrar_dique()
        barco_seleccion = int(input("Elige un barco por su número "))
        
        if barco_seleccion == 0:
            break
        
        if barco_seleccion not in TIPOS_BARCOS or TIPOS_BARCOS[barco_seleccion][1] <= 0:
            print("Seleccion no valida o barco agotado.")
            continue
        
        barco, cantidad = TIPOS_BARCOS[barco_seleccion]
        orientacion, altitud, longitud = obtener_coordenadas()
        
        if not validar_colocacion(barco, orientacion, altitud, longitud, tamanno_tablero, tablero_iniciado):
            print("El barco no cabe en esa posicion!")
            continue
        
        barco.fletar(orientacion, altitud, longitud, tablero_iniciado, 2)
        TIPOS_BARCOS[barco_seleccion] = (barco, cantidad - 1)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{barco.nombre} colocado!")
        print(tablero_iniciado[2])