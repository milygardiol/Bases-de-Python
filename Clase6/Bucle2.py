import os
os.system('cls')

email = input('Ingrese su email: ')

conta=0

#recorre cada uno de lo caracteres de una variable tipo texto, el bucle se repite tantas veces como caracteres tenga la variable 'email'

#un for nos permite recorrer texto caracter a caracter
for i in email:
    if i == '@':
        conta+=1
#la expresión equivale a poner conta=conta+1 operador '+='

if conta == 0:
    print('La dirección no contiene @')
elif conta == 1:
    print('La dirección tiene el formato correcto')
else:
    print('La dirección tiene más de un @')

