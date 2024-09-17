import os
os.system('cls')

#1 - un diccionario puede tener diferentes tipos de valores

diccionario2 = {
    'Codigo': 1001,
    'Color': 'Verde',
    'Talles': 'L',
    'Precio': 1200
}

print(diccionario2); input()


#2 - copiar un diccionario a otro
diccioanrio3 = diccionario2.copy()
print(diccionario2); input()

#3 - borrar un diccionario
diccioanrio3.clear()
print(diccioanrio3); input()

# 4 - ver TODAS las CLAVES de un diccionario

print(diccionario2.keys());input()


# 5 - ver TODOS los VALORES de un diccionarios

print(diccionario2.values());input()

