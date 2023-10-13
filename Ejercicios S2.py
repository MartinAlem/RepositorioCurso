# 1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es mayor de edad (18 años o más) o no.

edad = int(input('Por favor ingresa tu edad'))

if edad >= 18:
    print('Eres Mayor de Edad')
else:
    print('Eres Menor de Edad')


# 2-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es positivo, negativo o cero.

numero = int(input('Por favor ingresa un número entero: '))

if numero > 0:
    print('"POSITIVO"')
elif numero == 0:
    print('ES CERO')
else:
    print('"NEGATIVO"')


# 3-Escribir un programa que pida al usuario dos números y muestre por pantalla cuál de ellos es mayor.

num1 = float(input('por favor, ingresa un número: '))
num2 = float(input('por favor ingresa otro número: '))

if num1 > num2:
    print(f'El primer número ingresado: {num1} es mayor')
elif num1 < num2: 
     print(f'El segundo número ingresado: {num2} es mayor')
else:
     print(f'El primer número ingresado: {num1} es igual al segundo {num2}')


# 4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla si está aprobado (5 o más) o no.

nota_examen = float(input('Ingresa la nota de tu ultimo exámen de matemáticas:'))

if nota_examen >= 5:
    print('Excelente, Aprobaste !!!')
else:
    print('Estudia un poco más para la proxima: DESAPROBADO')


# 5-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero_entero = int(input('por favor, ingresá un número entero: '))

if numero_entero % 2 == 0:
    print(f'el número: {numero_entero}, es un numero PAR')
else:
    print(f'el número: {numero_entero}, es un numero IMPAR')


# 6-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es múltiplo de 2 y de 3 a la vez.

numero_entero = int(input('por favor, ingresá un número entero: '))

if numero_entero % 2 == 0 and numero_entero % 3 == 0:
    print(f'El número {numero_entero}, es multiplo de 2 y tambien de 3')
else:
    print(f'El número {numero_entero}, NO ES multiplo de 2 y 3 (ambos)')


# 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si es una letra mayúscula, una letra minúscula, un número o un carácter especial.

caracter = input('Por favor, ingresá un caracter: ')

# comprobamos si es mayuscula utiliznado .isupper
if caracter.isupper():
    print(f'El caracter ingresado, "{caracter}" es una letra en Mayusculas')

# comprobamos si es minuscula utiliznado .islower
elif caracter.islower():
    print(f'El caracter ingresado, "{caracter}" es una letra en Minusculas')

# comprobamos si es minuscula utiliznado .islower
elif caracter.isdigit():
    print(f'El caracter ingresado, "{caracter}" es un Número')

# comprobamos si es un caracter especial
else:
    print(f'El caracter ingresado, "{caracter}" es un caracter especial')


# 8-Escribir un programa que pida al usuario una cadena de caracteres y muestre por pantalla si contiene la letra "a".

cadena = input('Por favor ingresa una palabra o frase: ')

if "a" or "A" in cadena:
    print(f'la palabra o frase: "{cadena}", Contiene la letra a')
else:
    print(f'la palabra o frase: "{cadena}", No contiene la letra a')


# Otra Forma (con "find"):

cadena = input('Por favor ingresa una palabra o frase: ')
indice = cadena.find("a") # El metodo find va a devolver -1 si no encontro lo que busca. sino indica la posición en la que encontró la letra

if indice != -1:
    print(f'la palabra o frase: "{cadena}", Contiene la letra a')
else:
    print(f'la palabra o frase: "{cadena}", No contiene la letra a')


# Otra Forma 2 (con "count"), en el caso de Count es necesario pasar todo a minusculas porque detecta mayusculas y minusculas:

cadena = input('Por favor ingresa una palabra o frase: ')
cadena_minuscula = cadena.lower()
cantidad = cadena_minuscula.count("a") # El metodo count va a devolver el numero de veces que encuentre la letra a

if cantidad > 0:
    print(f'la palabra o frase: "{cadena}", Contiene la letra "a" {cantidad} veces')
else:
    print(f'la palabra o frase: "{cadena}", No contiene la letra a')


# 9-Escribir un programa que pida al usuario tres números y muestre por pantalla el mayor de ellos.

numero1 = int(input('por favor ingresa un número: '))
numero2 = int(input('por favor ingresa un número: '))
numero3 = int(input('por favor ingresa un número: '))

mayor = numero1

if numero2 > mayor:
    mayor = numero2

if numero3 > mayor:
    mayor = numero3

print(f'Ingresaste los números {numero1},{numero2} y {numero3}, el mayor de todos es {mayor}')


# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es una vocal o una consonante.

letra = input('Por favor ingresa una letra: ')
letra = letra.lower()

if letra in ("aeiou"):
    print ('Ingresaste una vocal')
elif letra.isalpha():
    print('Ingresaste una Consonante')
else:
    print('Ingresasta una caracter que no es una letra del alfabeto')


# otra forma:

letra = input("Introduce una letra: ")

if letra in ["a", "e", "i", "o", "u","A","E","I","O","U"]:
    print(f"La letra {letra} es una vocal.")
else:
    print(f"La letra {letra} es una consonante.")


# 11-Escribir un programa que pida al usuario dos números y muestre por pantalla la suma de ellos solo si ambos son pares.

n1 = int(input('ingresa un número: '))
n2 = int(input('ingresa otro número: '))

if n1 % 2 == 0 and n2 % 2 == 0:
    print(f'El resultado de sumar {n1} y {n2}, es: "{n1+n2}"')
else:
    print('Uno a ambos números no son pares')

# Otra Forma:

def es_par(numero):
    """
    Devuelve True si el número es par, False en caso contrario.
    Args:
        numero: El número a comprobar.
    Returns:
        True si el número es par, False en caso contrario.
    """
    return numero % 2 == 0

def main():
    """
    Programa principal.

    Pide al usuario dos números y muestra por pantalla la suma de ellos solo si ambos son pares.
    """
    numero_1 = int(input("Introduce un número: "))
    numero_2 = int(input("Introduce otro número: "))

    if es_par(numero_1) and es_par(numero_2):
        suma = numero_1 + numero_2
        print(f"La suma de {numero_1} + {numero_2} es {suma}.")
    else:
        print("Los números introducidos no son pares.")

if __name__ == "__main__":
    main()






