import random

INTENTOS_MAX = 6


def elegir_palabra():
    """Elige de una lista ya creada la palabra que sera usada durante
el ahorcado usando random.choice para elegir de lista de palabras y agregarlas a la lista
"""
    lista = []
    palabras = ["Barco", "Pirata", "Tesoro", "Cofre", "Espada", "Sirena", "Coco", "Garfio", "Parche", "Motin"]
    ahorcado = random.choice(palabras).upper()
    
    for i in range(len(ahorcado)):
        lista.append("_")  
    
    print("Palabra a adivinar:", lista)
    return ahorcado, lista


def int_jugador(ahorcado, lista):
    """Controla el flujo de turnos del jugador, la validación de entradas
    y determina la victoria o derrota al finalizar los intentos.
"""
    contador = 0
    letras_usadas = []

    while contador < INTENTOS_MAX and "_" in lista:
        ing = input("Adivina la letra, tu hija depende de ello: ").upper()
        
        
        while len(ing) != 1 or not ing.isalpha():
            ing = input("Solo ingresa una letra, tampoco ingreses un numero, recuerda lo que esta en juego: ").upper()
        
        if ing in letras_usadas:
            print("Ya ingresaste esa letra anteriormente. No te quitare un intento.")
            continue
        
        acierto = verificar_respuesta(ahorcado,lista,ing,contador)
        
        letras_usadas.append(ing)
        
        if acierto == False:
            contador += 1

    if "_" not in lista:
        print("Lograste descubrir la palabra y talvez salves a tu hija.")
        return True
        
    else:
        print("Has perdido el desafío. La palabra secreta era:", ahorcado)
        return False
            
    
    return ing


def verificar_respuesta(ahorcado,lista,ing,contador):
    """Verifica si la letra ingresada está en la palabra.
    Actualiza las posiciones descubiertas y devuelve True si acertó o False si falló.
"""
    if ing in ahorcado:    
        print("Correcto")
        for i in range(len(ahorcado)):
            if ahorcado[i] == ing:
                lista[i] = ing
            print(lista)
        return True
    else:
        print("Error - te quedan", (INTENTOS_MAX - contador), "intentos")
        print(lista)

        return False


                
        

ahorcado, lista = elegir_palabra()
int_jugador(ahorcado, lista)