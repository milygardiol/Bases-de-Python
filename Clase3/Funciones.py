
"""
SINTAXIS DE UNA FUNCIÓN

def nombre_funcion():
    instrucciones

 def nombre_funcion():
    instrucciones
    return valor

    hay que respetar la indentación

def nombre_funcion(argumentos):
    instrucciones de la función
    return/si return


"""

import os
os.system('cls')


def saludoAlumnos():
    print('Hola cómo están')
    print('ejemplo de funciones')

saludoAlumnos()

def promedioNotas():
    nota1=7
    nota2=6
    nota3=8
    promedio=(nota1+nota2+nota3)/3
    print(f'El promedio es: {promedio}')

promedioNotas()



def promedioNotas2(Nota1, Nota2, Nota3):
    promedio=(Nota1+Nota2+Nota3)/3
    print(f'El promedio con parámetros es: {promedio}')

promedioNotas2(9, 2, 5)