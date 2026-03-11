"""Módulo para configuración inicial."""

import os
import numpy as np
from .barco import TIPOS_BARCOS
from .partida import mostrar_tablero

def mostrar_dique():
    print("Barcos en el dique")
    for clave, (barco, cantidad) in TIPOS_BARCOS.items():
        if cantidad > 0:
            print(f"{clave}: {barco.nombre} tamano: {barco.tamanno} - cantidad: {cantidad}")


def obtener_coordenadas():
    while True:
        try:
            orientacion = int(input("Vertical(0) / Horizontal(1): "))
            
            if orientacion == 33:
                break
            elif orientacion not in [0, 1]:
                print("Por favor, introduce 0 para vertical o 1 para horizontal.")
                continue
                            
            altitud = int(input("Altitud del barco: ")) - 1
            if 0 > altitud > 9:
                raise ValueError
                        
            longitud = int(input("Longitud del barco: ")) - 1
            if 0 > longitud > 9:
                raise ValueError
                
            return orientacion, altitud, longitud
        except ValueError:
            print("Por favor, introduce valores numéricos válidos.")


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
        mostrar_tablero(tablero_iniciado[2])

        mostrar_dique()
        
        while True:
            try:
                barco_seleccion = int(input("Elige un barco por su número "))
                break
            except ValueError:
                print("Por favor, introduce un número válido.")
        
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
        mostrar_tablero(tablero_iniciado[2])