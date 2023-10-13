# Sentencia While
cont=0
suma=0
N = int(input('Ingrese tope máximo: '))
while cont <= N:
    suma = suma + cont
    cont = cont + 1
print('La suma total es: ', suma)


# Sentencia while con else
c = 0
while c <= 5:
    c += 1
    print('c vale :' c)
else:
    print('Se ha completado toda la iteración y c vale:', c)


# a) Sentencia For:

print('Comienzo')
for i in range(3):
    print('Hola ')
print('Final')

# b) Sentencia For:

print('Comienzo')
for i in range(3):
    print('Hola ', end='')  # La opción end='' evita que print agregue automáticamente un salto de línea después de imprimir la cadena, por lo que los "Hola" se imprimirán en la misma línea.
print('\nFinal')            #\n genera un salto e imprime Final en una nueva línea


# Instrucción break - continua con la siguiente instrucción (se puede usar con while y con for)

for letra in 'Python':
    if letra == 'h':
        break
    print('Letra Actual :', letra)
print('hemos llegado a la letra',letra)


# Instruccion Continue - vuelve al inicio del bucle

for letra in 'Python':
    if letra == 'h':
        continue
    print('Letra Actual :', letra)







