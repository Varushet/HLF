"""MODULO PARA CLASE BARCO"""

import numpy as np

class Barco:
    def __init__(self, nombre, tamanno):
        self.nombre = nombre
        self.tamanno = tamanno
    
    def slora(self):
        "Crea un array de numpy con el tamaño del barco en letras 'b'"
        return np.full(self.tamanno, "b", dtype=str)
    
    def fletar(self, orientacion, altitud, longitud, tablero_iniciado, posicion):
        if orientacion == 0:
            tablero_iniciado[posicion, altitud:altitud +self.tamanno, longitud] = self.slora()
        else:
            tablero_iniciado[posicion, altitud, longitud:longitud +self.tamanno] = self.slora()

TIPOS_BARCOS = {
    1: (Barco("Txalupa", 1), 4),
    2: (Barco("Bergantin", 2), 3),
    3: (Barco("Carabela", 3), 2),
    4: (Barco("Galeón", 4), 1)
    }