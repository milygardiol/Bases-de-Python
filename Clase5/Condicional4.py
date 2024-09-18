import os
os.system('cls')

print('-------Datos del comprador-------')

nombre = input('Nombre: ')
ciudad= input('Ciudad: ')
edad = int(input('Edad: '))

#calculo del descuento
#si el cliente es de córdoba, rosario o mendoza, tiene 20% de descuento
#si no vive en esas ciudades pero tiene entre 18 y 26 años, tiene 20% de descuento
#si no está en ninguno de estos casos, no posee descuento

if ciudad == 'cordoba' or ciudad == 'rosario' or ciudad == 'mendoza':
    descuento = 20
elif edad >= 18 and edad <= 26:
    descuento = 20
else:
    descuento = 0

print('El sr/sra ', nombre, f'tiene un descuento de {descuento}%')
