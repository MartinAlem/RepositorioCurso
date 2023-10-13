import random

# Lista de palabras predefinidas
palabras = ["python", "programacion", "juego", "computadora", "ahorcado"]

def seleccionar_palabra():
    # Seleccionar aleatoriamente una palabra de la lista
    return random.choice(palabras)

def jugar():
    palabra_secreta = seleccionar_palabra()
    palabra_oculta = "_" * len(palabra_secreta)
    intentos_restantes = 6
    letras_adivinadas = []
    letras_incorrectas = []

    # Mensaje de bienvenida y descripción del juego
    print("¡Bienvenido al Juego del Ahorcado!")
    print("En este juego, debes adivinar la palabra secreta letra por letra antes de quedarte sin intentos.")
    print("La palabra secreta tiene", len(palabra_secreta), "letras. ¡Buena suerte!\n")

    while intentos_restantes > 0 and palabra_oculta != palabra_secreta:
        # Mostrar el estado actual del ahorcado (opcional)
        ahorcado = [
            """
               ------
               |    |
                    |
                    |
                    |
                    |
            """,
            """
               ------
               |    |
               O    |
                    |
                    |
                    |
            """,
            """
               ------
               |    |
               O    |
               |    |
                    |
                    |
            """,
            """
               ------
               |    |
               O    |
              /|    |
                    |
                    |
            """,
            """
               ------
               |    |
               O    |
              /|\\   |
                    |
                    |
            """,
            """
               ------
               |    |
               O    |
              /|\\   |
              /     |
                    |
            """,
            """
               ------
               |    |
               O    |
              /|\\   |
              / \\   |
                    |
            """
        ]
        print(ahorcado[6 - intentos_restantes])

        # Mostrar la palabra oculta
        print("Palabra:", " ".join(palabra_oculta)) # Pone un espacio entre cada caracter de palabra oculta.
        print("Letras adivinadas:", ", ".join(letras_adivinadas))
        print("Letras incorrectas:", ", ".join(letras_incorrectas))
        
        # Solicitar al jugador que ingrese una letra
        while True:
            letra_ingresada = input("Ingresa una letra: ").lower()
            
            # Verificar si la letra ingresada es válida
            if len(letra_ingresada) == 1 and letra_ingresada.isalpha() and letra_ingresada not in letras_adivinadas + letras_incorrectas:
                break
            else:
                print("Letra inválida o ya ingresada. Intenta nuevamente.")

        # Verificar si la letra ingresada está en la palabra secreta
        if letra_ingresada in palabra_secreta:
            print("¡Correcto! La letra está en la palabra secreta.")
            letras_adivinadas.append(letra_ingresada)
            
            # Actualizar la palabra oculta con la letra adivinada
            nueva_palabra_oculta = ""
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra_ingresada:
                    nueva_palabra_oculta += letra_ingresada
                else:
                    nueva_palabra_oculta += palabra_oculta[i]
            palabra_oculta = nueva_palabra_oculta
        else:
            print("Incorrecto. La letra no está en la palabra secreta.")
            
            # Reducir el número de intentos restantes
            intentos_restantes -= 1
            
            # Registrar la letra como incorrecta
            letras_incorrectas.append(letra_ingresada)

    if palabra_oculta == palabra_secreta:
        print("¡Ganaste! Adivinaste la palabra secreta:", palabra_secreta)
    else:
        print("¡Perdiste! La palabra secreta era:", palabra_secreta)

    # Preguntar al jugador si quiere jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != 's':
        print("¡Gracias por jugar! Hasta la próxima.")

if __name__ == "__main__":
    jugar()
