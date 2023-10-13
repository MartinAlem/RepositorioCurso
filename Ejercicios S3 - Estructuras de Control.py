# 1-Escribe un programa que pida al usuario una palabra y luego imprima cada letra de la palabra en una línea separada.

palabra = input('por favor, ingresa una palabra: ')
    
for letra in palabra:
        print(letra)

#--------------------------------------------------------------------------------------------------------------------------
# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos los números naturales del 1 hasta ese número.

numero = int(input('Por favor, ingresá un número: '))

cont = 0
sum = 0

while cont < numero:
    cont += 1
    sum = sum + cont

print(f'Ingresaste el numero: {numero} ,la suma de todos los número desde el 1 al {numero}, es igual a: {sum}')

# Otra Solución Posible del Ejercicio 2:

# Pide al usuario un número
numero = int(input("Introduce un número: "))

# Inicializa la suma
suma = 0

# Recorre los números del 1 hasta el número introducido
for i in range(1, numero + 1):
    # Suma el número actual a la suma
    suma += i

# Imprime la suma
print("La suma es:", suma)

# El rango se define de 1 a numero + 1 porque la función range en Python genera una secuencia 
# de números que comienza en el primer argumento (inclusive) y termina antes del segundo argumento (exclusivo).

#----------------------------------------------------------------------------------------------------------------------
# 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de multiplicar 
# correspondiente a ese número del 1 al 10.

numero = int(input('Por favor, ingresa un número para armar su tabla de multiplicar: '))

for i in range(1, numero + 1):
    print(numero * i)

#-----------------------------------------------------------------------------------------------------------------------
# 4-Escribe un programa que imprima los números pares del 1 al 100.

for i in range(1,101):
     if i % 2 == 0:
          print(i)

# Explicación:
# Utilizamos un bucle for para iterar a través de los números del 1 al 100
for numero in range(1, 101):
    # Comprobamos si el número es par utilizando el operador %
    # Si el resultado de la división por 2 es igual a 0, el número es par
    if numero % 2 == 0:
        print(numero)

#------------------------------------------------------------------------------------------------------------------------
# 6-Escribe un programa que pida al usuario una palabra y luego imprima la misma palabra pero con las letras en orden inverso.

palabra = input('Por favor, ingresa una palabra: ')

palabra_inversa = palabra[::-1] 

print(palabra_inversa)

# Explicación:
#Ahora, en el contexto de revertir una cadena, utilizamos [::-1] como el rebanado. 
# Esto significa que estamos tomando toda la cadena (:) desde el principio (inicio omitido), 
# hasta el final (final omitido) pero con un paso de -1 (-1). Un paso de -1 significa que estamos 
# recorriendo la cadena en dirección inversa, lo que esencialmente revierte la cadena original
#Por lo tanto, cadena[::-1] devuelve la cadena original al revés.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7-Escribe un programa que pida al usuario una palabra y determine si es unpalíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).

palabra = input('Por favor, ingresá una palabra para evaluar si es unpalíndromo: ')

if palabra == palabra[::-1]:
     print(f'La palabra "{palabra}", es "unpalíndromo", es decir, se lee igual de adelante para atras o visceversa')
else:
     print(f'La palabra "{palabra}", no es "unpalíndromo"')

# SOLUCIÓN CHAT GPT:

# Solicita al usuario que ingrese una palabra
palabra = input("Por favor, ingresa una palabra: ")

# Convierte la palabra a minúsculas para hacer la comparación insensible a mayúsculas
palabra = palabra.lower()

# Revierte la palabra utilizando rebanado
palabra_al_reves = palabra[::-1]

# Comprueba si la palabra original es igual a la palabra al revés
if palabra == palabra_al_reves:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima el número de palabras que contiene

cadena_texto = input('por favor ingresa un texto: ')

Q_Caracteres = len(cadena_texto)
print(f'el texto que ingresaste tiene {Q_Caracteres} caracteres incluyendo los espacios')

Lista_Palabras = cadena_texto.split() # <-- Esto arma una lista con cada una de las palabras del texto. Ej ['la', 'casa', 'esta', 'en', 'orden']
print(Lista_Palabras) # Muestra --> ['la', 'casa', 'esta', 'en', 'orden']

Q_Palabras = len(Lista_Palabras)
print(f'El numero de palabras que tiene el texto ingresado es de: {Q_Palabras} Palabras')

# OTRAS SOLUCIONES PROPUESTAS POR CHAT GPT o BARD:

# BARD 1
cadena = "Hola mundo"

# Cuenta el número de palabras
numero_palabras = len(cadena.split())

# Imprime el número de palabras
print("El número de palabras es:", numero_palabras)

# BARD 2  es igual a uno pero con más pasos
cadena = "Hola mundo"

# Divide la cadena de texto en palabras
palabras = cadena.split()

# Cuenta el número de palabras
numero_palabras = len(palabras)

# Imprime el número de palabras
print("El número de palabras es:", numero_palabras)

# BARD 3
# BARD 3
import re

cadena = "Hola mundo"

# Divide la cadena de texto en palabras utilizando expresiones regulares
palabras = re.split(" ", cadena)

print(palabras) # <-- ['Hola', 'mundo']

# Cuenta el número de palabras
numero_palabras = len(palabras)

# Imprime el número de palabras
print("El número de palabras es:", numero_palabras)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# 9-Escribe un programa que pida al usuario un número y luego imprima la secuencia de Fibonacci correspondiente a ese número.

# Primero utilizariamos algunas de las formas que figuran debajo para generar una lista:

# Opción 1 - Una forma de Generar una lista:
numero = int(input('por favor, ingresa un número: '))

Lista_Numeros = list(range(0,numero+1))
print(Lista_Numeros)                   # <-- [0,1,2,3,4,5,6,7,8,9,10]


# Opcion 2 - Otra forma de Generar una lista a partir de un bucle For.
numero = int(input('por favor, ingresa un número: '))

Lista = []

for i in range(0,numero+1):
    Lista.append(i)

print(Lista)

# SOLUCIÓN DEL EJERCICIO:

# Pide al usuario un número
n = int(input("Introduce un número: "))

# Inicializa la secuencia de Fibonacci
fibo = [0, 1]

# Recorre la secuencia de Fibonacci
for i in range(2, n + 1):
    # Calcula el siguiente número de Fibonacci
    fibo.append(fibo[i - 1] + fibo[i - 2])

# Imprime la secuencia de Fibonacci
for i in fibo:
    print(i)

#----------------------------------------------------------------------------------------------------------------------------------------
# 10-Escribe un programa que pida al usuario una cadena de texto y luego imprima la misma cadena pero con todas las vocales en mayúscula.

# SOLUCION 1:

# Pide al usuario una cadena de texto
cadena = input("Introduce una cadena de texto: ")

# Reemplaza las vocales por sus mayúsculas correspondientes
cadena = cadena.replace("a", "A").replace("e", "E").replace("i", "I").replace("o", "O").replace("u", "U")

# Imprime la cadena de texto
print(cadena)

# # SOLUCION 2:

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Por favor, ingresa una cadena de texto: ")

# Crear una cadena vacía para almacenar la versión modificada
cadena_modificada = ""

# Definir las vocales en minúscula y mayúscula
vocales_minusculas = "aeiou"
vocales_mayusculas = "AEIOU"

# Recorrer la cadena de entrada
for caracter in cadena:
    # Si el caracter es una vocal en minúscula, conviértela a mayúscula
    if caracter in vocales_minusculas:
        caracter = caracter.upper()
    
    # Agregar el caracter a la cadena modificada
    cadena_modificada += caracter

# Imprimir la cadena modificada
print("La cadena con las vocales en mayúscula es:", cadena_modificada)

#--------------------------------------------------------------------------------------------------------------------------------------
# 11-Escribe un programa que pida al usuario un número y calcule su factorial.Un factorial es el producto que resulta de multiplicar un número entero positivo
# dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial de 4 es 4! = 4 × 3 × 2 × 1 = 24.

numero_factorial = int(input('por favor ingresa un número: '))

resultado = numero_factorial

for i in range(2,numero_factorial):
    resultado = resultado * i

print(resultado)

# OTRAS SOLUCIÓN

# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Por favor, ingresa un número entero positivo: "))

# Inicializar una variable para almacenar el factorial
factorial = 1

# Calcular el factorial del número
if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, numero + 1):
        factorial *= i

    # Imprimir el resultado
    print(f"El factorial de {numero} es {factorial}")





     
     













   

