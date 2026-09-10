User = "marco"
cont = "pirata"
intentos = 0
max_intentos = 2


def encriptar_contraseña(contraseña, corrimiento=3):
    """Encripta una cadena de texto desplazando el código ASCII de cada carácter

    según el valor de corrimiento especificado.

    :param contraseña: Cadena de texto plano a encriptar.
    :param corrimiento: Número de posiciones a desplazar cada carácter (por defecto 3).
    :return: Cadena de texto encriptada.
    """
    return "".join(chr(ord(caracter) + corrimiento) for caracter in contraseña)


def validar_credenciales():
    """Solicita usuario y contraseña, encripta la clave ingresada y valida las credenciales.

    Permite hasta un número máximo de intentos fallidos antes de denegar el acceso.

    :param usuario_registrado: Nombre de usuario válido.
    :param contrasena_encriptada: Contraseña almacenada en formato encriptado.
    :param max_intentos: Número máximo de intentos permitidos.
    :return: True si la autenticación fue exitosa, False en caso contrario.
    """
    intentos = 0
    while intentos < max_intentos:
        Usuario = input("Ingrese su usuario: ")
        contraseña = encriptar_contraseña(input("Ingrese su contraseña: "))
        if Usuario == User and contraseña == cont:
            print("¡Bienvenido!")
            return True,cont
        else:
            print("Usuario o contraseña incorrectos. Intente nuevamente.")
            intentos += 1
            intentos_restantes = max_intentos - intentos

            if intentos_restantes > 0:
                print(f"Le quedan {intentos_restantes} intentos.")
            else:
                print("Ha excedido el número máximo de intentos. Acceso denegado.")

    return False



def sala_1():
    
    print("\n--- SALA 1: EL CAMAROTE DEL CAPITÁN ---")
    print("La puerta está cerrada. En el escritorio encuentras una nota:")
    print('"Tengo teclas, pero no abro cerraduras. Tengo espacio, pero no soy una habitación. ¿Qué soy?"')

    respuesta = input("Escribe tu respuesta: ").strip().lower()
    if respuesta in ("teclado", "un teclado", "el teclado"):
        print("Correcto. El teclado activa el mecanismo de la puerta.")
        return True

    print("La respuesta es incorrecta. La puerta permanece cerrada.")
    return False


def sala_2():
    print("\n--- SALA 2: LA BODEGA ---")
    print("Entras a la bodega y encuentras tres cofres: rojo, azul y verde.")
    print("Solo uno contiene la llave. Las inscripciones dicen:")
    print("Rojo: La llave no está en el cofre azul.")
    print("Azul: La llave está en este cofre.")
    print("Verde: La inscripción del cofre azul es falsa.")
    print("Solo una de las tres inscripciones es verdadera.")

    respuesta = input("¿Qué cofre eliges? ").strip().lower()
    if respuesta in ("azul", "cofre azul"):
        print("Correcto. Encuentras la llave y completas la segunda sala.")
        return True

    print("Ese cofre está vacío. El desafío no ha sido superado.")
    return False


def jugar():
    """Inicia la narrativa del Escape Room y controla el flujo secuencial entre salas,

    requiriendo superar la Sala 1 (Ahorcado) para avanzar a la Sala 2 (Batalla Naval).
    """
    print("\n========== EL BARCO FANTASMA ==========")
    print("Una tormenta te ha dejado atrapado en un barco abandonado.")
    print("La tripulación desapareció y una niebla extraña rodea la embarcación.")
    print("Para escapar, deberás investigar el barco y resolver sus desafíos.")
    print("Cada sala conduce a la siguiente: primero debes superar un desafío")
    print("para poder continuar el recorrido.")

    print("\nEl recorrido comienza en el camarote del capitán.")
    if not sala_1():
        print("\nEl recorrido termina en la Sala 1. Regresa a Jugar para intentarlo de nuevo.")
        return

    print("\nLa puerta de la bodega se abre. Has desbloqueado la Sala 2.")
    if sala_2():
        print("\n¡Has completado las Salas 1 y 2 del Escape Room!")
    else:
        print("\nEl recorrido termina en la Sala 2. Regresa a Jugar para intentarlo de nuevo.")


def cambiar_contraseña(cont):
    """Permite al usuario cambiar su contraseña validando que la contraseña actual sea correcta

    y que la nueva clave cumpla con todas las reglas de seguridad del sistema.

    :param contrasena_actual_enc: Contraseña encriptada vigente.
    :return: Nueva contraseña encriptada si el cambio fue exitoso, o la contraseña actual si falló.
    """
    contraseña_actual = encriptar_contraseña(
        input("Ingrese su contraseña actual: ")
    )

    if contraseña_actual != cont:
        print("La contraseña actual es incorrecta.")
        return

    nueva_contraseña = input("Ingrese la nueva contraseña: ")
    confirmacion = input("Confirme la nueva contraseña: ")

    if not nueva_contraseña:
        print("La contraseña no puede estar vacía.")
    elif nueva_contraseña != confirmacion:
        print("Las contraseñas no coinciden.")
    elif len(nueva_contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
    elif not any(c.islower() for c in nueva_contraseña):
        print("La contraseña debe tener al menos una minúscula.")
    elif not any(c.isupper() for c in nueva_contraseña):
        print("La contraseña debe tener al menos una mayúscula.")
    elif " " in nueva_contraseña:
        print("La contraseña no puede contener espacios.")
    elif encriptar_contraseña(nueva_contraseña) == cont:
        print("La nueva contraseña no puede ser igual a la actual.")
    else:
        cont = encriptar_contraseña(nueva_contraseña)
        print("Contraseña modificada correctamente.")


def mostrar_menu():
    """Despliega el menú principal de la aplicación y gestiona la navegación del usuario

    entre instrucciones, inicio del juego, cambio de clave y cierre de sesión.

    :param usuario_registrado: Usuario autenticado en la sesión.
    :param contrasena_encriptada: Contraseña encriptada actual de la sesión.
    """
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("0. Instrucciones del juego")
        print("1. Jugar")
        print("2. Cambiar contraseña")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("\nInstrucciones del juego: ")
        elif opcion == "1":
            jugar()
        elif opcion == "2":
            cambiar_contraseña(cont)
        elif opcion == "3":
            print("Cerrando sesión...")
            return
        else:
            print("Opción no válida.")


cont = encriptar_contraseña("pirata")

if validar_credenciales():
    mostrar_menu()








