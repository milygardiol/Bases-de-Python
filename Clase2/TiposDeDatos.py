

#Numéricos

#Enteros (int) 5, 8, 200
a = 10
b = 11
#Coma flotante (float)
c = 11.98
#Complejos
d = 3 + 4j



#Textos
#Ej: Juan, Montevideo, Paris 322, luis@jj.com
nombre = 'Juan'
apellido = 'García'
email = 'luis@jj.com'
direccion = 'Paris 322 - Montevideo'


#Booleanos
#True or false
esCasado = False
def estaSoltero():
    if esCasado == True:
        print('El señor está casado.')
        estaSoltero(True)
    else:
        print('Está soltero')
        estaSoltero(False)
    
    return estaSoltero()

estaSoltero()