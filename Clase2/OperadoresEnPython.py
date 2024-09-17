"""Aritméticos
        suma = +
        resta = -
        multiplicación = *
        división = /
        potenciación = **
        módulo = %
        división entera = //
"""



"""Comparación
        igual que = ==
        diferente que = !=
        mayor que = >
        menor que = >
        mayor o igual que = >=
        menor o igual que = <=
        
    Tienen relación con los lógicos

        AND = y
        OR = o
        NOT = no

    Especiales

        IS = es
        IS NOT = no es
        IN = dentro de
"""

"""Asignación

    igual = =
    igual sumar +=
    igual restar -=
    igual multiplicar *=
    igual dividir /=
    igual módulo %=
    igual potencia **=
    igual división entera //=

"""


import os
os.system('cls')

print('1 - CREAR UNA VARIABLE - EN ESTE CASO DE TIPO TEXTOS.')
nombre = 'Juan'
apellido = 'Pérez'

print('Variables + texto')
print('¡Hola ' + nombre + apellido + '!, ¿cómo estás?')


print('2- mejorar salida impresa')
print('¡Hola ', nombre ,' ', apellido, '!, ¿cómo estás?')

print('3- pedir información al usuario')
print('4 - mejorando la entrada de datos por pantalla')

#función input => le da la información a la variable de lo que ingrese el usuario
nom = input('Ingrese su nombre: ').capitalize()
ape = input('Ingrese su apellido: ').upper()

print('Hola, ', nom, ' ', ape, ' cómo estás?')


print('5 - agregamos un dato más, un número')

nombre_usuario = input('Ingrese su nombre: ')
apellido_usuario = input('Ingrese su apellido: ')

edad_usuario = input('Ingrese su edad: ')

print('Le damos la bienvenida ', nombre_usuario, ' ', apellido_usuario, ' ', 'edad: ', edad_usuario)


print('6 - solicitando datos de tipo numérico por pantalla')

precio1 = input('Introzca el precio: ')
precio2 = input('Introduzca un segundo precio: ')
total = precio1+precio2
print('El precio total es: ', total)
#en este caso no va a comprender que se trata de un tipo de dato numérico y solo va a concatenar los datos en sí

print('7 - convertir datos de tipo texto a entero e imprimir una salida concatenando un texto con un número')

#función int() convierte valores de tipo string a número entero
precio1 = int(input('Introduzca el primer precio: '))
precio2 = int(input('Introduzca el segundo precio: '))
total = precio1 + precio2

#f: format
#combinación de un valor de tipo texto y numérico

print(f'El precio total es: {total}')


print('8 - Operaciones matemáticas')
numero1=int(input('Introduzca el 1er valor: '))
numero2 = int(input('Introduzca el 2do valor: '))

print(f'Los valores para operar son: {numero1} y {numero2}')

calculo = numero1 + numero2
print(f'La suma es: {calculo}')
calculo = numero1 - numero2
print(f'La resta es: {calculo}')
calculo = numero1 * numero2
print(f'La multiplicación es: {calculo}')
calculo = numero1 /numero2
print(f'La división es: {calculo}')
calculo = numero1 ** numero2
print(f'La potencia es: {calculo}')
calculo = numero1 % numero2
print(f'El módulo es: {calculo}')
calculo = numero1 // numero2
print(f'La división entera es: {calculo}')
