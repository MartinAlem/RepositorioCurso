----------------------------------------------------------------------------------------------------------------------
# 1-Crea una función llamada suma que tome dos números como parámetros y devuelva la suma de ellos.

def suma(a,b):
    return a + b

resultado = suma(10,25)
print(resultado)


-----------------------------------------------------------------------------------------------------------------------
# 2-Crea una función llamada saludo que tome el nombre de una persona como parámetro e imprima un saludo personalizado.

def saludo(nombre):
    return print(f'hola, {nombre} te extrañamos por aqui. Bienvenido !!')

nombre = input('Ingresa tu nombre por favor: ')
saludo(nombre)


------------------------------------------------------------------------------------------------------------------------
# 3-Crea una función llamada invertir_cadena que tome una cadena de texto como parámetro y devuelva la cadena invertida.

def invertir_cadena(cadena_texto):
    texto_invertido = cadena_texto[::-1]
    return print(texto_invertido)

Texto_Ingresado = input('Buen día, por favor ingresa una texto cualquiera: ')
invertir_cadena(Texto_Ingresado)


--------------------------------------------------------------------------------------------------------------------------
# 4-Crea una función llamada es_capicua que tome un número como parámetro y 
# devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
# derecha a izquierda) y False en caso contrario.

def es_capicua(numero):     
    numero_original = numero
    numero_str = str(numero)
    numero_str_invertido = numero_str[::-1]
    numero_invertido = int(numero_str_invertido)

    print(numero_original)
    print(numero_str)
    print(numero_str_invertido)
    print(numero_invertido)

    if numero_original == numero_invertido:
        
        return True
        #return print(f'El número ingresado {numero} es Capicua')
    else:
        return False

numero = int(input('por favor ingresá un número: '))
Resultado = es_capicua(numero)
print(Resultado)


----------------------------------------------------------------------------------------------------------------
# 5-Crea una función llamada es_divisible que tome dos números enteros como
# parámetros y devuelva Es divisible si el primer número es divisible por el
# segundo número, o No es divisible en caso contrario.

def es_divisible(a,b):
    if a % b == 0:
        return print(f'{a} Es Divisible por {b}')
    else:
        return print(f'{a} no es divisible por {b}')

num1 = int(input('por favor ingresa un número: '))
num2 = int(input('por favor ingresa otro número: '))

es_divisible(num1,num2)
resultado = es_divisible(num1,num2)


------------------------------------------------------------------------------------------------------------------
# 6-Crea una función llamada es_par que tome un número como parámetro y
# devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
# devuelva Es impar o No es par

def es_par(num):
    if num == 0:
        return(f'El numero ingresado es {num}')
    elif num == 1:
        return(f'El numero ingresado es {num}')
    else:
        if num % 2 == 0:
            return(f'El numero ingresado {num} es Par')

num = input('Por favor ingresa un número, te indicaremos si es par: ')
es_par(num)


-------------------------------------------------------------------------------------------------------------------
# 7-Crea una función llamada imprimir_pares que tome un número entero como
# parámetro e imprima todos los números pares desde 1 hasta ese número.

# Opción 1 -----------------------------------------------------
def obtener_numero():
    num = int(input('Por favor, ingresá un número: '))
    return num

def imprimir_pares(num):
    for i in range(2, num + 1, 2):
        print(i)

if __name__ == "__main__":
    num = obtener_numero ()
    imprimir_pares(num)

# Opción 2 -----------------------------------------------------
def obtener_numero():
    num = int(input('Por favor, ingresá un número: '))
    return num

def imprimir_pares(num):
    for i in range(num):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
  num = obtener_numero()
  imprimir_pares(num)

-------------------------------------------------------------------------------------------------------------------
# 8-Crea una función llamada es_palindromo que tome una cadena de texto como
# parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
# de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso contrario.

def obtener_texto():
    return input('Por favor ingresa una palabra o texto: ')

def es_palindromo(c_texto):
    """
    Devuelve es palindromo si la cadena de texto especificada es un palíndromo, o
    no es palindromo en caso contrario.

    Args:
        cadena: La cadena de texto a evaluar.

    Returns:
        True si la cadena de texto es un palíndromo, o False en caso contrario.
    """
    c_texto_al_reves = c_texto[::-1]
    
    if c_texto == c_texto_al_reves:
        print(f'la palabra o frase, {c_texto}, es "Palíndromo" porque al reves se escribe igual {c_texto_al_reves}')
    else:
        print(f'la palabra o frase, {c_texto}, no es "Palíndromo" porque al reves se escribe: {c_texto_al_reves}')


if __name__ == "__main__":
    c_texto = obtener_texto()
    es_palindromo(c_texto)

# Solución Bard:

def es_palindromo(cadena):
  """
  Devuelve es palindromo si la cadena de texto especificada es un palíndromo, o
  no es palindromo en caso contrario.

  Args:
    cadena: La cadena de texto a evaluar.

  Returns:
    True si la cadena de texto es un palíndromo, o False en caso contrario.
  """

  cadena = cadena.lower()  # Convertimos la cadena a minúsculas.
  cadena = cadena.strip()  # Eliminamos los espacios en blanco al principio y al
  # final de la cadena.

  # Invertimos la cadena de texto.
  cadena_invertida = cadena[::-1]

  # Comparamos la cadena original con la cadena invertida.
  if cadena == cadena_invertida:
    return True
  else:
    return False


if __name__ == "__main__":
  cadena = input("Ingrese una cadena de texto: ")
  resultado = es_palindromo(cadena)

  if resultado:
    print("La cadena de texto es un palíndromo.")
  else:
    print("La cadena de texto no es un palíndromo.")


# Solución ChatGPT:

def es_palindromo(cadena):
    # Elimina los espacios en blanco y convierte la cadena a minúsculas
    cadena = cadena.replace(" ", "").lower()
    
    # Comprueba si la cadena es igual a su inversa
    return cadena == cadena[::-1]

# Ejemplo de uso
cadena = "anilina"
if es_palindromo(cadena):
    print(f"'{cadena}' es un palíndromo.")
else:
    print(f"'{cadena}' no es un palíndromo.")

---------------------------------------------------------------------------------------------------
# 9-Crea una función llamada promedio que tome una lista de números como
# parámetro y devuelva el promedio de esos números.

def promedio(lista_numeros):
    
    suma_lista = sum(lista_numeros)
    print(f'la suma de todos los números de la lista es igual a: {suma_lista}')
    
    cant_num_lista = len(lista_numeros)
    print(f'la cantidad de números de la lista es igual a: {cant_num_lista}')

    promedio = suma_lista / cant_num_lista

    return promedio

if __name__ == "__main__":

    lista_numeros = [1,3,8,9,10]
    resultado = promedio(lista_numeros)

    print(f'el promedio de esta lista de números {lista_numeros} es igual a: {resultado}')

---------------------------------------------------------------------------------------------------















