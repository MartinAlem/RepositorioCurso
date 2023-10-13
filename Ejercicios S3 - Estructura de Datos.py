#EJERCICIOS DE ESTRUCTURA DE DATOS:

#-----------------------------------------------------------------------------------------------------------------------
# 1-Crear un diccionario con los nombres de tres frutas y sus respectivos precios y mostrar el diccionario completo.

diccionario_frutas = {
    "Manzana": 1200, 
    "Banana": 1000,
    "Anana": 2400,
}
print(diccionario_frutas)

#------------------------------------------------------------------------------------------------------------------------
# 2-Crear una lista con los nombres de tres ciudades y agregar una cuarta ciudad al final de la lista.

lista_ciudades = ['Roma','New York','Paris']
print(lista_ciudades)

lista_ciudades.append('Madrid')
print(lista_ciudades)

#-------------------------------------------------------------------------------------------------------------------------
# 3-Crear una lista con los nombres de tres países y mostrar el segundo país de la lista.

lista_paises = ['Argentina','Brasil','Noruega']
print(lista_paises)

print(lista_paises[1])

#-------------------------------------------------------------------------------------------------------------------------
# 4-Crear un diccionario con los nombres de tres personas y sus respectivas edades. Mostrar la edad de la tercera persona en el diccionario.

diccionario_persona_edad = {
    'Martin':46,
    'Mariela':46,
    'Nahuel':16,
    'Gian':12,
}

print(diccionario_persona_edad)

print(diccionario_persona_edad ['Nahuel'])

#------------------------------------------------------------------------------------------------------------------------------
# 5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número más grande en el conjunto.

conjunto_numeros = {1,2,3,4,5,6,7,8,9,10}
print(conjunto_numeros)
print(type(conjunto_numeros))

numero_mas_grande_del_conjunto = max(conjunto_numeros)
print(numero_mas_grande_del_conjunto)

#-------------------------------------------------------------------------------------------------------------------------------
# 6-Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número de elementos en el conjunto.

set_numeros_impares = {1,3,5,7,9}
print(set_numeros_impares)
elementos_del_set = len(set_numeros_impares)
print(elementos_del_set)

#-------------------------------------------------------------------------------------------------------------------------------
# 7-Crear un diccionario con los nombres de tres ciudades y sus respectivas poblaciones. Agregar una cuarta ciudad al diccionario 
# con su respectiva población. Mostrar el diccionario resultante.

diccionario_ciudades = {
    'Moscú': 3000000,
    'Helsinski': 1000000,
    'Oslo':2000000
}

print(diccionario_ciudades)

diccionario_ciudades.update({'La Paz': 1500000}) # en este paso agregamos una ciudad con su población al diccionario

print(diccionario_ciudades)

#-----------------------------------------------------------------------------------------------------------------------------------
# 8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso.

#Estas son dos formas distintas de crear una lista de números del 1 a 10
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_numeros1 = list(range(1, 11))

print(lista_numeros)
print(lista_numeros1)

lista_numeros.reverse()
print(lista_numeros)

#-----------------------------------------------------------------------------------------------------------------------------------
# 9-Crear una lista con los nombres de tres países y ordenar la lista en orden alfabético. Mostrar la lista resultante.

lista_3_paises = ['Japon', 'Nigeria', 'Australia']
print(lista_3_paises)

lista_3_paises.sort()
print(lista_3_paises)

#-----------------------------------------------------------------------------------------------------------------------------------
# 10-Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la lista. Mostrar la lista resultante.

lista_3_frutas = ['Durazno','Pera','Mamon']
print(lista_3_frutas)

del lista_3_frutas[1]
print(lista_3_frutas)

#------------------------------------------------------------------------------------------------------------------------------------
# 11-Crear una lista con los nombres de tres animales y agregar una cuarta animal al principio de la lista. Mostrar la lista resultante.

lista_3_animales = ['Oso','Puma','Aguila']
print(lista_3_animales)

lista_3_animales.insert(0,'Perro')
print(lista_3_animales)

#------------------------------------------------------------------------------------------------------------------------------------
# 12-Crear una lista con los nombres de tres países y reemplazar el segundo país de la lista por otro país. Mostrar la lista resultante.

lista_3_paises = ['Argelia','Ruanda','Costa de Marfil']
print(lista_3_paises)

lista_3_paises[1] = 'India'
print(lista_3_paises)

#-------------------------------------------------------------------------------------------------------------------------------------
# 13-Crear una lista con los nombres de tres colores y agregar dos colores más al final de la lista. Mostrar la lista resultante.

lista_3_colores = ['Rojo','Blanco','Verde']
print(lista_3_colores)
lista_3_colores.append ('Anaranjado')
lista_3_colores.append ('Violeta')
print(lista_3_colores)

# Otra Forma:
print('Ahora de otra forma')
lista_3_colores = ['Rojo','Blanco','Verde']
print(lista_3_colores)
lista_3_colores += ['Azul','Rosado']
print(lista_3_colores)

#-----------------------------------------------------------------------------------------------------------------------------------
# 14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los elementos de la tupla.

tupla_Numeros = (1,2,3,4,5)
print(tupla_Numeros)
print(type(tupla_Numeros))

suma_tupla = sum (tupla_Numeros)
print(suma_tupla)



