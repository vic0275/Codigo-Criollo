from random import choice


TAMAÑO = 5
CANTIDAD_BARCOS = 3
MAX_DISPAROS = 12


def armar_tablero(valor):
    """Crea una matriz cuadrada de TAMAÑO x TAMAÑO inicializada con un valor determinado.

    :param valor: El valor inicial para rellenar las celdas del tablero (ej. 0 o '-').
    :return: Matriz (lista de listas) que representa el tablero.
    """
    matriz = []
    for fila in range(TAMAÑO):
        nueva_fila = []
        for columna in range(TAMAÑO):
            nueva_fila.append(valor)
        matriz.append(nueva_fila)
    return matriz


def entra_barco(tablero, fila, columna):
    """Verifica si un barco puede ubicarse en la coordenada dada sin solaparse

    ni quedar adyacente (horizontal, vertical o diagonalmente) a otro barco.

    :param tablero: Matriz de enteros que representa el tablero oculto.
    :param fila: Índice de la fila a evaluar (0 a TAMAÑO-1).
    :param columna: Índice de la columna a evaluar (0 a TAMAÑO-1).
    :return: True si la casilla y sus adyacentes están libres, False en caso contrario.
    """
    for fila_vecina in range(fila - 1, fila + 2):
        for columna_vecina in range(columna - 1, columna + 2):
            if 0 <= fila_vecina < TAMAÑO and 0 <= columna_vecina < TAMAÑO:
                if tablero[fila_vecina][columna_vecina] == 1:
                    return False
    return True


def poner_barcos():
    """Verifica si un barco puede ubicarse en la coordenada dada sin solaparse

    ni quedar adyacente (horizontal, vertical o diagonalmente) a otro barco.

    :param tablero: Matriz de enteros que representa el tablero oculto.
    :param fila: Índice de la fila a evaluar (0 a TAMAÑO-1).
    :param columna: Índice de la columna a evaluar (0 a TAMAÑO-1).
    :return: True si la casilla y sus adyacentes están libres, False en caso contrario.
    """
    tablero = armar_tablero(0)
    for barco in range(CANTIDAD_BARCOS):
        posiciones_validas = []
        for fila in range(TAMAÑO):
            for columna in range(TAMAÑO):
                if entra_barco(tablero, fila, columna):
                    posiciones_validas.append([fila, columna])

        posicion = choice(posiciones_validas)
        fila = posicion[0]
        columna = posicion[1]
        tablero[fila][columna] = 1
    return tablero


def mostrar_tablero(tablero_visible):
    """Imprime en pantalla el estado actual del tablero visible con sus cabeceras

    de filas y columnas.

    :param tablero_visible: Matriz con el estado descubierto por el jugador ('-', 'X', 'O').
    """
    print("\n    1 2 3 4 5")
    for fila in range(TAMAÑO):
        print(fila + 1, " |", end=" ")
        for columna in range(TAMAÑO):
            print(tablero_visible[fila][columna], end=" ")
        print()
    print("- = sin explorar | X = barco hundido | O = agua")


def pedir_coordenada(nombre):
    """Solicita al usuario el ingreso de una coordenada (Fila o Columna) y valida

    que sea un número entero dentro del rango permitido (1 a TAMAÑO).

    :param nombre: Nombre del eje a solicitar ("Fila" o "Columna").
    :return: Entero convertido a índice base 0.
    """
    dato = input(nombre + " (1 a 5): ").strip()
    while dato not in ["1", "2", "3", "4", "5"]:
        print("Entrada inválida. Escribí un número entero del 1 al 5.")
        dato = input(nombre + " (1 a 5): ").strip()
    return int(dato) - 1


def elegir_casilla(tablero_visible):
    """Solicita al usuario el ingreso de una coordenada (Fila o Columna) y valida

    que sea un número entero dentro del rango permitido (1 a TAMAÑO).

    :param nombre: Nombre del eje a solicitar ("Fila" o "Columna").
    :return: Entero convertido a índice base 0.
    """
    fila = pedir_coordenada("Fila")
    columna = pedir_coordenada("Columna")
    while tablero_visible[fila][columna] != "-":
        print("Ya disparaste ahí. Elegí otra posición; no perdés un disparo.")
        fila = pedir_coordenada("Fila")
        columna = pedir_coordenada("Columna")
    return fila, columna


def disparar(tablero_oculto, tablero_visible, fila, columna):
    """Evalúa el impacto del disparo en la coordenada seleccionada, actualiza

    el tablero visible e informa el resultado.

    :param tablero_oculto: Matriz con la ubicación real de los barcos.
    :param tablero_visible: Matriz visible que se actualizará con 'X' o 'O'.
    :param fila: Índice de la fila atacada.
    :param columna: Índice de la columna atacada.
    :return: True si se hundió un barco (impacto), False si fue agua.
    """
    if tablero_oculto[fila][columna] == 1:
        tablero_visible[fila][columna] = "X"
        print("¡IMPACTO! Barco hundido.")
        return True
    tablero_visible[fila][columna] = "O"
    print("AGUA")
    return False


def mostrar_avance(hundidos, disparos):
    """Muestra en pantalla las estadísticas actuales del jugador: barcos hundidos,

    barcos restantes y disparos disponibles.

    :param hundidos: Cantidad de barcos destruidos hasta el momento.
    :param disparos: Cantidad de disparos restantes.
    """
    print("Barcos hundidos:", hundidos)
    print("Barcos restantes:", CANTIDAD_BARCOS - hundidos)
    print("Disparos disponibles:", disparos)


def jugar_batalla_naval():
    """Función principal de la Sala 2. Coordina la creación del juego, los turnos de disparo

    y determina las condiciones de victoria o derrota.

    :return: True si el jugador hundió todos los barcos, False si se agotaron los disparos.
    """
    tablero_oculto = poner_barcos()
    tablero_visible = armar_tablero("-")
    hundidos = 0
    disparos = MAX_DISPAROS

    mostrar_tablero(tablero_visible)
    mostrar_avance(hundidos, disparos)

    while disparos > 0 and hundidos < CANTIDAD_BARCOS:
        fila, columna = elegir_casilla(tablero_visible)
        impacto = disparar(tablero_oculto, tablero_visible, fila, columna)
        disparos = disparos - 1
        if impacto:
            hundidos = hundidos + 1
        mostrar_tablero(tablero_visible)
        mostrar_avance(hundidos, disparos)

    if hundidos == CANTIDAD_BARCOS:
        print("¡Ganaste! Hundiste toda la flota y superaste la sala 2.")
        return True

    print("Perdiste: te quedaste sin disparos. El recorrido termina acá.")
    return False
