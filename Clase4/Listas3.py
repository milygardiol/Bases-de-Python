import os
os.system('cls')

#ordenamiento de listas

Lista2 = ['Araceli', 'Laura', 'Juan', 'Irene', 'Samuel', 'Jose', 'Laura']

#1 - formas de ordenar una lista

Lista2.reverse()
#invierte el orden natural de la lista
print(Lista2); input()

#ordenar alfabéticamente, si está compuesta de números los ordena de menor a mayor
Lista2.sort()
print(Lista2); input()

#ordenar alfabéticamente a la inversa
Lista2.sort(reverse = True)
print(Lista2); input()


#2 - formas de buscar un valor en una lista

a = Lista2.count('Laura')
print(a); input()

a = Lista2.count('XXXX')
print(a); input()

a = Lista2.index('Juan')
print(a); input()

