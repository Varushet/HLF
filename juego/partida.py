"""Módulo para la lógica de disparos."""
import os
from .enemigo import disparar_bot

def mostrar_tablero(tablero):
    """Imprime el tablero con índices de filas y columnas."""
    print("    " + "  ".join(str(i) for i in range(1, 11)))
    for i, fila in enumerate(tablero, 1):
        print(f"{i:2}  " + "  ".join(fila))
    print()

def disparo(i, j, tablero_iniciado):
    '''
    Recive las coordenadas de la función entrada() para comprobar si en el sitio
    había o no un barco y volver a efectuar otro disparo o no.
    '''

    if tablero_iniciado[0, i-1, j-1] in ("b", "d"):
        print("¡Tocado!")
        tablero_iniciado[1, i-1, j-1] = "x"
        tablero_iniciado[0, i-1, j-1] = "x"
        input("")
        victoria(tablero_iniciado)
        apuntar(tablero_iniciado)
    else:
        print("¡Agua!")
        tablero_iniciado[1, i -1, j -1] = "O"
        input("")
        disparar_bot(tablero_iniciado)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TU TABLERO ===")
    mostrar_tablero(tablero_iniciado[2])
    print("=== TABLERO DE DISPAROS ===")
    mostrar_tablero(tablero_iniciado[1])
    disparar_bot(tablero_iniciado)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TU TABLERO ===")
    mostrar_tablero(tablero_iniciado[2])
    print("=== TABLERO DE DISPAROS ===")
    mostrar_tablero(tablero_iniciado[1])


def apuntar(tablero_iniciado):
    '''
    Entrada del juego, con validación robusta de la entrada del usuario.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TU TABLERO ===")
    mostrar_tablero(tablero_iniciado[2])
    print("=== TABLERO DE DISPAROS ===")
    mostrar_tablero(tablero_iniciado[1])

    while True:
        try:
            print("0 para salir")
            i = int(input("Apunta a la fila: "))
            j = int(input("Y a la columna: "))

            if i == 0 or j == 0:
                print("Saliendo...")
                exit()

            if i < 1 or i > 10 or j < 1 or j > 10:
                print("Fuera de rango!")
                continue

            disparo(i, j, tablero_iniciado)
            return

        except ValueError:
            print("Por favor, introduce valores numéricos válidos.")

def victoria(tablero_iniciado):
    enemigos_vivos = False
    for i in range(10):
        for j in range(10):
            if tablero_iniciado[0, i, j] in ("b", "d"):
                enemigos_vivos = True
                break
        if enemigos_vivos:
            break

    if not enemigos_vivos:
        print("Has Ganado!!!")
        exit()

    jugador_vivo = False
    for i in range(10):
        for j in range(10):
            if tablero_iniciado[2, i, j] in ("b", "d"):
                jugador_vivo = True
                break
        if jugador_vivo:
            break

    if not jugador_vivo:
        print("Has perdido!!!")
        exit()

    return False