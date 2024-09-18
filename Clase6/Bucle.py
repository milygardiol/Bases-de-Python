"""
ESTRUCTURA BUCLE

Una estructura de bucle es aquella que se usa para repetir una o un grupo de líneas de código varia veces.

Existen dos estructuras en python que se llaman FOR y WHILE

En el caso de FOR la cantidad de veces que se repite el bucle es determinada y conocida de antemano.

WHILE la cantidad de veces que se repite el bucle es indeterminada y dependerá de condiciones que se planteen en el programa.
"""

import os
os.system('cls')

lista = ['Araceli', 'Laura', 'Juan', 'Irene', 'Samuel', 'Jose', 'Laura']

#hacer bucles para cada valor de la lista

print('Recorrer la lista')

#'lis' tomará los valores de la lista
#la cantidad de ciclos que hará el for es igual a la cantidad de elementos de la lista.

for lis in lista:
    print(lis)

#hacer bucles 7 veces que es la cantidad de elementos de la lista
#recordar que el primer valor es cero y el último es un valor más que el último índice de la lista (6) = (6 + 1).

print('Recorrer la lista nuevamente')

#recorremos con el 'rango' => hará los ciclos que le indico

for i in range (0, 7):
    print(lista[i])

#print(i) me mostraría el valor numérico de la variable i
#print(lista[i]) muestra el valor de la posición i de la lista
