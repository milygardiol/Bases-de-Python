"""

El diccionario es una estructura de datos que, al igual que las listas y tuplas, permite almacenar valores de diverso tipo

A diferencia de aquellas estructuras, lo datos se almacenan de a pares siendo el primer elemento de par la clave y el segundo elemento el valor propiamente dicho. De ese modo se crea una asociación tipo clave:valor

Los elementos almacenados no están ordenados.

SINTAXIS

Diccionario={clave1:valor1, clave2:valor2, clave3:valor3, ...}


"""

import os
os.system('cls')

#1 - creación

diccionario1 = {
    'FCB': 'Barcelona',
    'CHE': 'Chelsea',
    'MIL': 'Milán',
    'PSG': 'Paris SG'
}

print(diccionario1); input()

#2 - ver un elemento del diccionario por su clave
print(diccionario1['CHE']); input()


#3 - agregar un elemento
diccionario1['RMA'] = 'real madrid'
print(diccionario1); input()

#4 - modificar un elemento
diccionario1['RMA'] = 'Real Madrid'
print(diccionario1); input()

#5 - eliminar un elemento
del diccionario1 ['CHE']
print(diccionario1); input()



