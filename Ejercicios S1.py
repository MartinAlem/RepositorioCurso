#-----------------------------------------------------------------------------------------------------
# EJERCICIO 1-Escribe un programa que solicite al usuario su nombre y lo imprima en la pantalla.
# Solicitar el nombre al usuario
nombre = input("¿Cómo te llamas?")

# Imprimir el nombre en la pantalla
print(f"Hola {nombre}")

# Así quedaría el programa completo:
nombre = input("¿Hola, Cómo te llamas?")
print(f'Hola {nombre}')

# --------------------------------------------------------------------------------------------------
# EJERCICIO 2-Escribe un programa que solicite al usuario su nombre y luego imprima un mensaje de bienvenida.

nombre = input('¿Cómo te llamas?')
print(f'Bienvenido {nombre}')

# --------------------------------------------------------------------------------------------------
# EJERCICIO 3-Crea un programa que pida al usuario su edad y lo imprima en pantalla.

edad = input('¿Que edad tienes?')
print (f'Entonces tienes {edad} años')

# --------------------------------------------------------------------------------------------------
# EJERCICIO 4-Crea un programa que calcule la suma de dos números y lo imprima en pantalla.

# Solicitar los números al usuario
numero1 = int(input("Introduce el primer número: ")) # si no pongo Int python lo puede tomar como str?
numero2 = int(input("Introduce el segundo número: ")) # si no pongo Int python lo puede tomar como str?

# Calcular la suma
suma = numero1 + numero2

# Imprimir la suma en pantalla
print(f"La suma de los dos números es: {suma}")

# ---------------------------------------------------------------------------------------------------
# EJERCICIO 5-Crea un programa que pida al usuario dos números enteros y muestre en pantalla su cociente y su resto.

# Solicitar los números al usuario
numero1 = int(input('Introduce el primer número entero'))
numero2 = int(input('Introduce el segundo número entero'))

# Calcular el Cociente
cociente = numero1 // numero2
resto = numero1 % numero2

# Imprimir el Cociente y el Resto en Pantalla
print(f'El Cociente es: {cociente}')
print(f'El Resto es: {resto}')

#---------------------------------------------------------------------------------
# EJERCICIO 6-Crea un programa que pida al usuario el radio de un círculo y calcule su área.
#La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
#Supongamos que pi = 3.1416

PI = 3.1416
radio = int(input('Introduce un valor entero que represente el radio de un circulo'))

area_circulo = PI * (radio ** 2)

print(area_circulo)

# EJERCICIO 6 - Otra forma

import math # Invocamos la biblioteca math

# Solicitamos al usuario el radio del círculo
radio = float(input("Introduce el radio del círculo: "))

# Calculamos el área del círculo
area = math.pi * radio**2

# Imprimimos el resultado en pantalla
print("El área del círculo es:", area)

#-----------------------------------------------------------------------------
# EJERCICIO 7
# Escribe un programa que calcule el área de un triángulo a partir de la base y la altura dadas.

triangulo_base = float(input('Ingresa la base del triangulo: '))
triangulo_altura = float(input('Ingresa la altura del triangulo: '))

triangulo_area = (triangulo_base * triangulo_altura) / 2

print(triangulo_area)

# OTRA FORMA:

# Solicitamos al usuario la base y la altura del triángulo
base = float(input("Introduce la base del triángulo: "))
altura = float(input("Introduce la altura del triángulo: "))

# Calculamos el área del triángulo
area = (base * altura) / 2

# Imprimimos el resultado en pantalla
print("El área del triángulo es:", area)

# -------------------------------------------------------------------------------------
# EJERCICIO 8 Crea un programa que pida al usuario el radio de un círculo y muestre su
# diámetro, su circunferencia y su área. Supón que pi es aproximadamente 3.14159.

pi = 3.14159
radio = float(input('Ingresa el radio del circulo: '))

diametro = 2 * radio
circunferencia = 2 * pi * radio
area = pi * radio**2

print(f'Estas son las medidas del Circulo, Diámetro: {diametro}, Circunferencia: {circunferencia}, Área: {area}')

# Otra Forma:
# Importamos la biblioteca math para poder utilizar la constante pi
import math

# Solicitamos al usuario el radio del círculo
radio = float(input("Introduce el radio del círculo: "))

# Calculamos el diámetro del círculo
diametro = 2 * radio

# Calculamos la circunferencia del círculo
circunferencia = 2 * math.pi * radio

# Calculamos el área del círculo
area = math.pi * radio**2

# Imprimimos los resultados en pantalla
print("El diámetro del círculo es:", diametro)
print("La circunferencia del círculo es:", circunferencia)
print("El área del círculo es:", area)

# --------------------------------------------------
# EJERCICIO 9 - Escribe un programa que solicite al usuario dos números y luego imprima la
# suma, la resta, la multiplicación y la división de los dos números.

n1 = float(input('Ingresa un número'))
n2 = float(input('Ingresa otro número'))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

print ('el resultado de la suma de ambos numeros es: ',suma)
print ('el resultado de la resta de ambos numeros es: ',resta)
print ('el resultado de la multiplicación de ambos numeros es: ',multiplicacion)
print ('el resultado de la división de ambos numeros es: ',division)

# Otra forma:
# Solicitamos al usuario dos números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Calculamos las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Imprimimos los resultados
print("La suma de los dos números es:", suma)
print("La resta de los dos números es:", resta)
print("La multiplicación de los dos números es:", multiplicacion)
print("La división de los dos números es:", division)

# ---------------------------------------------------------------------------------------
# EJERCICIO 10 - Crea un programa que pida al usuario una cantidad en dólares y la convierta a
# euros. Supón que el tipo de cambio es de 0.84 euros por dólar.

dolares = float(input('ingresa el monto en dolares: '))
euros = dolares * 0.84

print(f'La conversión es, Dolares {dolares} = {euros} Euros')

# ---------------------------------------------------------------------------------------
# EJERCICIO 11 - Crea un programa que pida al usuario una palabra y muestre en pantalla
# cuántas letras tiene. Pss psssss toma... .len()

palabra = input('Ingresa una palabra o frase: ')
print(f'El número total de caracteres incluyendo espacios si corresponde es de: {len(palabra)}')

# ---------------------------------------------------------------------------------------
# EJERCICIO 12 - Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# dd/mm/aaaa y luego imprima su edad en años. Utiliza la función .split()

import datetime

# Solicitamos al usuario su fecha de nacimiento
fecha_nacimiento = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

# Dividimos la fecha de nacimiento en una lista
fecha_nacimiento_lista = fecha_nacimiento.split('/') # Fecha_nacimiento_lista = ['07','06','1977']

# Obtenemos el año de nacimiento
año_nacimiento = int(fecha_nacimiento_lista[2])

# Obtenemos el año actual
año_actual = int(datetime.datetime.today().strftime("%Y"))

# Calculamos la edad
edad = año_actual - año_nacimiento

# Imprimimos la edad
print("Tu edad es de", edad, "años.")

# Paso 1 - pido al usuario que ingrese la fecha de nacimiento con un determinado formato
fecha_nacimiento = input('Por favor, ingresa tu fecha de nacimiento en formato dd/mm/aaaa')

# Paso 2 - convierto la fecha en una lista. uso la función .split para lograrlo
fecha_nacimiento_lista = fecha_nacimiento.split('/')

# Paso 3 - Pruebo como quedo conformada la lista
print(fecha_nacimiento_lista)

# Otra Forma:
# Paso 1 - pido al usuario que ingrese la fecha de nacimiento con un determinado formato
fecha_nacimiento = input('Por favor, ingresa tu fecha de nacimiento en formato dd/mm/aaaa: ')

# Paso 2 - convierto la fecha en una lista. uso la función .split para lograrlo
fecha_nacimiento_lista = fecha_nacimiento.split('/')

# Paso 3 - Pruebo como quedo conformada la lista
print(fecha_nacimiento_lista)

# Paso 4 - Extraigo el año de Nacimiento
año_nacimiento = int(fecha_nacimiento_lista[2])

# Paso 5 - Compruebo que este obteniendo bien el año de nacimiento
print(año_nacimiento)

# Paso 6 - Obtengo el año actual - para esto invoco la libreria datetime
import datetime
año_actual = int(datetime.datetime.today().strftime('%Y'))
print(año_actual)

#Paso 7 - Obtengo la Edad

edad = año_actual - año_nacimiento
print(f'Tienes {edad} años de edad')

# ---------------------------------------------------------------------------------------
# EJERCICIO 13 - 








# --------------------------------------------------
# OTROS EJERCICIOS
# DISTINTAS FORMAS PARA CALCULAR EL PROMEDIO DE NOTAS

# FORMA 1
notas = [6, 8, 8, 8, 9]

promedio = 0
for nota in notas:
    promedio += nota

promedio = promedio / len(notas)

print(promedio)

# FORMA 2
notas = [4,5,2,10,6]

sum_notas = 0
for nota in notas:
    sum_notas = sum_notas + nota

q = len(notas)

promedio = sum_notas / q

print(promedio)

# FORMA 3
notas = [6, 8, 8, 8, 9]

suma_notas = 0 # Acumulador
num_notas = 0  # Contador

for nota in notas:
    suma_notas += nota
    num_notas += 1

promedio = suma_notas / num_notas


# FORMA 4 (Sin for)
notas = [6, 8, 8, 8, 9]
#print('El promedio de notas es: ',sum(notas)/len(notas))
print(f'El promedio de notas es: {sum(notas)/len(notas)}')