#append()
#extend()
#insert()
#pop()
#remove()


import os
os.system('cls')

Lista2=['Javier', 'Laura', 'Irene', 'Matias', 'Jose']

#1- formas para agregar datos
Lista2.append('Juan')
print(Lista2); input()

#"ampliar/extender" la lista (deben estar con corchetes, coma y comillas)
Lista2.extend(['Marcela', 'Claudia'])
print(Lista2); input()

#agregar un elemento en un lugar determinado
#hay que agregar el índice más el dato a agregar
Lista2.insert(0, 'Ramiro')
print(Lista2); input()

#2. métodos de eliminación

Lista2.pop()
print(Lista2); input()

Lista2.pop(3)
print(Lista2); input()

Lista2.remove('Laura')
print(Lista2); input()
