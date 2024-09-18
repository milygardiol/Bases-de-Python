import os
os.system('cls')

def calificacion (nota):
    if nota <5:
        condicion = 'Reprobado'
    else:
        condicion = 'Aprobado'
    return condicion

print('------------------------------')
print('-----CALIFICACIÓN ALUMNOS-----')
print('------------------------------')

nota = int(input('Ingrese la nota del alumno: '))
condicion = calificacion(nota)
print('El alumno queda: ', condicion)
