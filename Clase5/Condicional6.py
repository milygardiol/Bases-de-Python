import os
os.system('cls')

print('-----calculo del descuento-----')
sede = int(input('Introduzca la sede (1- central 2-otras): '))
edad = int(input('Introduzca su edad: '))

#sede central: si tiene +65 20% desc, sino 0%
#otras sedes: si tiene +65 15% desc, si tiene +40 10% desc, sino 0%

#bucles anidados
if sede == 1:
    if edad >= 65:
        descuento = 20
    else:
        descuento = 0
elif sede == 2:
    if edad >= 65:
        descuento  = 15
    elif edad >= 40:
        descuento = 10
    else:
        descuento = 0
    

print('El descuento para el cliente es de: ', descuento)