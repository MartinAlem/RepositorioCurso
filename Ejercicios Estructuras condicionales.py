# ESTRUCTURAS CONDICIONALES
# ---------------------------------
# IF Encadenados 

print('Ejercicio de IF Encadenados ') 
edad = 14

if edad >= 16:
    print('Usted puede votar')
if edad < 16:
    print ('Usted no puede votar')

#----------------------------------
# IF Anidados

print('Ejercicio de IF Anidados ') 
edad1 = 17
edad2 = 25

if edad1 >= 16:
    print('Usted puede votar')
    if edad2 >= 21:
        print('Usted tambien puede viajar al exterior')

#----------------------------------
# Uso de Operadores Lógicos como IF

print('Ejercicio de Operadores lógicos utilizados como IF')
usuario = 'informatorio2023'
contraseña = 'info2023'

if usuario == 'informatorio2023' and contraseña == 'info2023':
    print('Acceso Correcto. Bienvenido')

#----------------------------------
# Uso de Operadores Lógicos como IF-ELSE

print('Ejercicio de IF-ELSE')
usuario = 'informatorio2023'
contraseña = 'contraseña_incorrecta'

if usuario == 'informatorio2023' and contraseña == 'info2023':
    print('Acceso Correcto. Bienvenido')
else:
    print('Contraseña Incorrecta. por favor volve a ingresar los datos')

#----------------------------------
# Uso de Operadores Lógicos como IF-ELIF
print('Ejercicio de ELIF')

nota1 = 7
nota2 = 8   
nota3 = 10

promedio = round(((nota1 + nota2 + nota3) / 3), 2)

if promedio < 6:
    print('por lo vist no estudiaste lo suficiente, DESAPROBASTE')
elif promedio < 8:
    print('Aprobaste, Muy Bien !!')
else:
    print(f'Super Excelente, tus promedio de notas fue: {promedio}') 