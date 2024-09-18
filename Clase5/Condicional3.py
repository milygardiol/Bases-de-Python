import os
os.system('cls')

# 0-2: recursante 3-4: reprobado 5-6: aprobado 7-10: promocionado
#cuando hay más argumentos debemos usar 'elif'

def calificacion (nota):
    if nota <= 2:
        condicion = 'Recursante'
    elif nota <= 4:
        condicion = 'Reprobado'
    elif nota <= 6:
        condicion = 'Aprobado'
    else:
        condicion = 'Promocionado'
    return condicion


print('------------------------------')
print('-----CALIFICACIÓN ALUMNOS-----')
print('------------------------------')

nota = int(input('Ingrese la nota del alumno: '))
condicion = calificacion(nota)
print('El alumno queda: ', condicion)
