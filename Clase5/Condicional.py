"""
Condicionales:
    es importante la indentación
    las instrucciones dentro del condicional van a ejecutarse en caso de que la condición sea verdadera, sino, sigue con las demás instrucciones.
"""

import os
os.system('cls')

def calificacion(nota):
    condicion = 'Aprobado'
    if nota < 5:
        condicion = 'Reprobado'
    return condicion



print('------------------------------')
print('-----CALIFICACIÓN ALUMNOS-----')
print('------------------------------')

#primero pido el valor al usuario y lo guardo en la variable 'nota'
nota=int(input('Ingrese la nota del alumno: '))

#el resultado de la función con el argumento de nota se guardará en una variable 'condición'
#no tiene nada que ver con la condición de la función interna, cada variable tiene vida útil donde sea implementada

condicion = calificacion(nota)

print('El alumno queda: ' + condicion)
