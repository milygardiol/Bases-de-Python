"""
La tupla es una estructura similar a una Lista pero sus características son inalterables, esto es, no se pueden agregar, eliminar o midificar el valor de sus elementos.

Las tuplas son más rápidas que las listas y hacen un uso más efectivo del espacio de memoria.
SINTAXIS:
    Tupla=(valor1, valor2, valor3)

"""

#1 - creación

Tupla1=(1, 2, 3)
Tupla2=('Javier', 'Laura', 'Irene', 'Matias', 'Jose')
Lista3=['Juan Perez', 45, True]


#método 'tuple' más la lista de base para crear la tupla
Tupla3=tuple(Lista3)

#2 - acceder a los datos
print(Tupla2); input()
print(Tupla2[3]); input()
print(Tupla3[2]); input()

#medir la longitud de las tuplas
print(len(Tupla1)); input()
print(len(Tupla2)); input()

#¿cuántas veces está el valor '45' en la tupla?
print (Tupla3.count(45)); input()

#tres variables separadas igualadas a la tupla
#cada uno de los valores de la tupla 3 serán asignados a las variables 'nombre, edad, casado'
nombre, edad, casado = Tupla3

#cadena con valores tipo string y función format para combinar el texto con variables numéricas
print('El sr ', nombre, f' tiene {edad} años')