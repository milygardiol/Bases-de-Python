import os
os.system('cls')


#lista de provincias
ListaProv=['cordoba', 'entre rios', 'mendoza', 'san juan', 'chubut', 'salta']
print('-------Datos del comprador-------')

nombre = input('Nombre: ')
provincia= input('Provincia: ')
edad = int(input('Edad: '))

#cálculo del descuento
"""
Operador especial IN (significa EN) irve para ver si un elemento está EN (dentro) de un conjunto
de elementos.
"""
if provincia in ListaProv:
    descuento = 20
elif edad >=18 and edad <= 26:
    descuento =20
else:
    descuento = 0


print('El sr/sra ', nombre, f'tiene un descuento de {descuento}%')

